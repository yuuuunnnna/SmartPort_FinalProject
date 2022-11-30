# FinalProject_항만보안관제시스템

디지털스마트부산아카데미_최종프로젝트

항만보안사고 예방 프로젝트_ 지능형 CCTV를 이용한 항만 내 관제 시스템 
### **요약**

- 디지털 스마트 부산 아카데미에서 기업연계 프로젝트로 진행한 스마트 항만 최종 프로젝트
- 매년 막대한 예산 투입에도 불구하고 항만 내 보안사고가 꾸준히 발생 및 증가하고 있는 문제 해결 방안으로 지능형 CCTV 도입을 통한 항만 보안 관제 시스템 프로젝트 진행
- 항만 내 특정 구역 지정 후, 사람 침입 감지 시 소리 경보 및 문자 메시지 전송 기능 서비스 구현
- 향후 항만 내 드론, RC카 등 도구를 이용하여 2차 보안 예방에도 적용 가능

### **시기**

- 2022.10.17 ~ 2022. 11.22 ( 총 약 5주간 진행)

### **역할**

- 총 5명이 함께 진행 (기획, 제안, 데이터구축, 모델학습, 서비스 구현)
- Roboflow 데이터 선별, Selenium을 사용한 웹사이트 이미지 크롤링을 통한 이미지 데이터셋 구축
- 기획 및 제안서 작성
- Yolov5 모델학습 진행

### **성과**

- 동의대학교 ICT 공과대학장상 수상

---

### 설계(기획안)

- 기획안 미리보기
 <img width="389" alt="image" src="https://user-images.githubusercontent.com/73158757/204795483-dccbe49c-9070-4cdb-8621-67c4856151be.png">
    
<img width="386" alt="image" src="https://user-images.githubusercontent.com/73158757/204795539-10e497ee-c6a7-4716-888f-c62815df55cd.png">
    
<img width="412" alt="image" src="https://user-images.githubusercontent.com/73158757/204795597-4464ddb6-b112-44b6-b500-0febd4344b93.png">

<img width="416" alt="image" src="https://user-images.githubusercontent.com/73158757/204795646-dab07a36-c231-46b9-962a-f1c57a1c0c6f.png">

---

### 데이터셋 구축

<img width="281" alt="image" src="https://user-images.githubusercontent.com/73158757/204795158-07319a88-6da8-40fb-b201-51df3025b105.png">

---

### 모델 학습

<img width="466" alt="image" src="https://user-images.githubusercontent.com/73158757/204795720-66c47ce1-b215-41d3-9602-8b6d746db8f9.png">


---

### 학습 / 기능 구현 도구

- PyTorch
- Jupyter notebook
- Colab
- Yolov5
- Yolov7
- OpenCV

---

### 서비스 흐름도

<img width="447" alt="image" src="https://user-images.githubusercontent.com/73158757/204795792-995b5757-2301-4e9c-bb49-b40eff1a7216.png">

---

### 기능

<img width="441" alt="image" src="https://user-images.githubusercontent.com/73158757/204795871-33d55d4f-31e1-4163-b378-089b0343778f.png">

- 마우스를 이용하여 침임 감지영역 설정 (총 4개의 점으로 다각형 생성)
- 침입 감지영역에 사람 객체가 닿게 되면 경보음 출력 및 캡쳐
- 캡쳐화면 Telegram 메신저로 침입 장면 이미지 전송

---

### 결과 및 활용 방안

- 인건비 절감 효과
    - 기존에는 관제요원 1인당 최대 48대 CCTV 모니터링, 지능형 CCTV 도입시 1인 최대 400대까지 관제 가능 기대
    - 부산항에 적용 시 인건비,교육비, 훈련비 등등 약 32억 예산 절약 예상 도출
- 실시간 침입 탐지에 따른 선제적 보안 예방
- 실시간 모니터링으로 신속대응
- 지능형 CCTV 도입으로 인한 업뭄 강도 완화 및 보안강화 기대

<img width="433" alt="image" src="https://user-images.githubusercontent.com/73158757/204795948-7403632c-f177-4d09-91af-d26947f85d91.png">

침입감지 외에도 사람 탐지 기능으로 군중밀집 지역에 지능형 CCTV 도입으로 인원 수 파악 및 위험 관리 에도 활용 가능
