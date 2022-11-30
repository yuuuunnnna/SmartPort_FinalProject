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

[_1팀_지능형CCTV_기획안_.hwp](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/54fb1910-b9ac-4e98-bef2-b1b5f863895f/_1%E1%84%90%E1%85%B5%E1%86%B7_%E1%84%8C%E1%85%B5%E1%84%82%E1%85%B3%E1%86%BC%E1%84%92%E1%85%A7%E1%86%BCCCTV_%E1%84%80%E1%85%B5%E1%84%92%E1%85%AC%E1%86%A8%E1%84%8B%E1%85%A1%E1%86%AB_.hwp)

- 기획안 미리보기
    
    ![스크린샷 2022-11-30 오후 6.01.41.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/276ae9dc-ad36-4207-b2f7-87158a94267c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-11-30_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.01.41.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5aa3d1f6-7dc6-4fbf-aba6-35f612703e11/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2d01653-cb45-4d25-ac38-72033dcafd6a/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/af1682dd-985e-4232-aef5-6f195a31ec64/Untitled.png)
    

---

### 데이터셋 구축

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f2a44d56-5999-40d5-8b23-c3fef4d98233/Untitled.png)

---

### 모델 학습

![스크린샷 2022-11-30 오후 6.14.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7fa81a8-5a37-40df-8890-abfaa0d1dac1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-11-30_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.14.10.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d925346-aca8-430d-83d5-465507cca65f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b6173806-4c4f-43f1-a29e-5ac9f6f6ba1b/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2d106aa9-5dd0-4711-8411-b0ce086ccdfe/Untitled.png)

---

### 기능

![스크린샷 2022-11-30 오후 5.40.10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cce3091-1fd2-4d02-a959-a6bcc7b2068b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-11-30_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.40.10.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/17bf223a-af96-4266-9f73-c9eebc98e697/Untitled.png)

침입감지 외에도 사람 탐지 기능으로 군중밀집 지역에 지능형 CCTV 도입으로 인원 수 파악 및 위험 관리 에도 활용 가능
