import torch
import numpy as np
import cv2
import telegram as tel
import threading
from pygame import mixer
from shapely.geometry import Polygon

mixer.init() #Initialzing pyamge mixer

mixer.music.load('GANADARA.mp3') #Loading Music File


def send_tele(word):
   bot = tel.Bot(token="5503523524:AAFqRO1K0Xx1fTmI5c6NNWcPp_0Q06BeByU")
   chat_id =  5581126225 #-1001873940891  
   image = 'cap.png'
   image2 = 'picture.png'
   bot.sendMessage(chat_id=chat_id, text=word)
   bot.send_photo(chat_id = chat_id, photo=open(image, 'rb'))
   bot.send_photo(chat_id = chat_id, photo=open(image2, 'rb'))

#모델 다운로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
#model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/best.pt')  # local model
#model = torch.hub.load('C:/Users/Administrator/Desktop/yolov5', 'custom', path='C:/Users/Administrator/Desktop/yolov5/yolov5x6.pt', source='local')  # local repo

#클래스 0번만 적용
model.classes = [0]

# 폰트 색상 지정
blue = (255, 0, 0)
green= (0, 255, 0)
red= (0, 0, 255)
white= (255, 255, 255)
black= (0,0,0)

#FontFace 설정
FontFace =  cv2.FONT_HERSHEY_PLAIN

#카메라 0번
cap = cv2.VideoCapture(cv2.CAP_ANY + 1)

#화면크기 변수
ScreenWidth = 1280
ScreenHeight = 800

#폰트 크기
FontScale = 2
if ScreenWidth<800:
    FontScale = FontScale*0.5
    
#person 위치 변수
PersonScreenWidth = round(ScreenWidth*0.8)
PersonScreenHeight = round(ScreenHeight*0.1)

PersonScreenWidth2 = round(ScreenWidth*0.7)
PersonScreenHeight2 = round(ScreenHeight*0.2)

#화면크기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, ScreenWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, ScreenHeight)

#첫 탐지
FirstDetect = False

#사람 탐지 유무
DetectPerson = 0

#FrameCount = 0

PointList = []

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 Down
        if len(PointList) < 4:
            PointList.append((x, y))
#동영상 저장
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.mp4', fourcc, 10, (frame_width,frame_height))

#opencv webcam
while cap.isOpened():
    ret, frame = cap.read()
    
    out.write(frame)
    #키입력 무한대기
    key = cv2.waitKey(10) & 0xFF
    if DetectPerson == False:
        cv2.imwrite('picture.png', frame)
    # Make detections
    
    results = model(frame)
    
    #랜더링
    ResultRender =np.squeeze(results.render())
    if len(PointList) >0:
        for i in range(len(PointList)):
            cv2.circle(ResultRender, PointList[i], 10, green, cv2.FILLED)
    #객체 데이터 프레임
    ResultsDf = results.pandas().xyxy[0]
    #print(ResultsDf)
    
    ResultsDfName = ResultsDf['name'] # 이름 column
    ResultsDfXmin = ResultsDf['xmin'] # xmin column
    ResultsDfXmax = ResultsDf['xmax'] # xmax column
    ResultsDfYmin = ResultsDf['ymin'] # ymin column
    ResultsDfYmax = ResultsDf['ymax'] # ymax column
    
    LenResultsDf = len(ResultsDf)
    PersonCount = 0
    DetectPersonCount = 0
    
    for i in range(LenResultsDf):
        if ResultsDfName[i]=='person':
            PersonCount = PersonCount +1
            
            RXmin = ResultsDfXmin[i]
            RXmax = ResultsDfXmax[i]
            RYmin = ResultsDfYmin[i]
            RYmax = ResultsDfYmax[i]
            
            if len(PointList) == 4:
                points1 = np.array(PointList)
                p1 = Polygon(points1)
                cv2.polylines(ResultRender, [points1], True, green, 2)
                pp=[(RXmin,RYmin),(RXmax,RYmin),(RXmax,RYmax),(RXmin,RYmax)]
                points2 = np.array(pp)
                p2 = Polygon(pp)
                if p1.intersects(p2) == True:
                    
                    DetectPersonCount = DetectPersonCount + 1
                    if DetectPerson == 0:
                        DetectPerson =1
                            
    if DetectPerson == 1:
        cv2.imwrite('cap.png', ResultRender)
                            
        #os.popen('"./siren2.mp3"')# 경보음 재생    
        #music.start()              
        mixer.music.play()                                     
        
        #threading.Thread(target=send_tele, args=(f'경고 : 거수자 {PersonCount}명이 침입', )).start()
        DetectPerson = 2                     

        
    if PersonCount>0:
        cv2.putText(ResultRender,f'Person:{PersonCount}', (PersonScreenWidth, PersonScreenHeight), FontFace, FontScale, blue, 1, cv2.LINE_AA)
    
    if DetectPersonCount > 0:
        cv2.putText(ResultRender,f'Detected person:{DetectPersonCount}', (PersonScreenWidth2, PersonScreenHeight2), FontFace, FontScale, white, 1, cv2.LINE_AA)
            
    cv2.imshow('BigBrother', ResultRender)
            
    cv2.setMouseCallback('BigBrother', mouse_handler)
        
    if key == ord('r'):
        PointList.clear()
        DetectPerson = 0
        mixer.music.stop()
        
    elif key == ord('w'):
        DetectPerson = 0
        
        mixer.music.stop()
    elif key == ord('q'):
        break


cap.release()
out.release()

cv2.destroyAllWindows()