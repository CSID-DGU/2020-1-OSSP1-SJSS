# 2020-1-OSSP1-SJSS-4
김준경, 김수희, 강성희, 이슬기입니다. 

## 주제
object detection을 활용한 Scratch X 라이브러리 생성

## 핵심 기술
object detection(사물인식) 
using tensorflow c api :
![tensorflow(object detection)](https://user-images.githubusercontent.com/59370701/80907325-30464380-8d51-11ea-89aa-92bc55afc1fa.JPG)

## 목적
기존의 텍스트 코딩과 달리 스크립트를 블록 맞추듯이 연결하여 코딩을 하는 방식으로 게임이나 애니메이션 등을 만들 수 있고, 비전공자도 쉽게 사용할 수 있는 교육용 프로그래밍 언어인 스크래치에 object detection 기술을 접합한 아두이노용 라이브러리를 생성한다.

## 관련 오픈소스
https://github.com/mohammedari/tensorflow_object_detector_ros/tree/master/src

## 프로젝트 내용

#### 2. 주제 선정 이유
- Scratch 프로그램은 어렸을 때 한 번쯤 다 사용해 본 경험이 있음
- Scratch api가 공개 되어있음
- object detection 관련 오픈 소스가 여러 가지 언어로 배포 되어있음
- 팀원이 모두 machine learning에 관심이 있음
- Scratch와 아두이노를 연결했을 때 시각적으로 결과물을 보임으로써 작동 원리를 깊게 이해 할 수 있음

#### 3.시스템 목표 및 세부사항
##### 카메라를 통해 인식한 사물에 대한 반응 작업에 대한 코드를 작성할 수 있음
- 편리성 제공
	: 블록 코딩 사용을 사용하여 코드 작성 작업을 단순화
- 사물 인식 
	: 카메라 연결, 사물을 인식하여 객체로 사용
- 머신러닝
	: 텐서플로우를 이용, 사물인식에 대한 정확도 향상
- 아두이노와 연결 / 아두이노 작동
	: 해당 코드에 알맞은 작동

#### 4. 개발범위 및 개발환경
##### 4-1. 개발범위

 - object detection 기능
        : 객체를 인식하여 프로그램이 객체에 따라서 상황에 맞는 코드가 실행되게 함.
 - library 추가 기능
        : 사용자가 원할 때, 라이브러리를 추가할 수 있도록 함.
 - scratch 확장 기능
        : 기존의 스크래치 프로그램에 vision에 관련한 기능을 추가하여 사용자들이 다양한 코드를 생성할 수 있도록 함.

##### 4-2. 개발환경
###### 라이브러리 확장
 -  파이어폭스 웹
 -  스크래치 프로그램
 -  js파일로 라이브러리 확장
 -  sbx파일로 프로젝트 생성 후 js파일 실행
###### Object detection
 -  ROS 
 -  vs (visual studio) 
 -  opencv (영상 인식)
 
#### 5. 관련 기술 및 시장 제품
##### 5-1. 관련 기술
- 머신 러닝
- Object Detection(사물 인식)
- 블록 코딩 
 
##### 5-2. 시장 제품
- Scratch : 교육 플랫폼
- Scratch X → 아두이노와 연결 가능
- Entry(엔트리) 

#### 6. 시스템 형상
![ossp1](https://user-images.githubusercontent.com/62641007/81142308-4d298380-8faa-11ea-8cf2-efdd6f14563e.PNG) 
![ossp2](https://user-images.githubusercontent.com/62641007/81142314-50247400-8faa-11ea-96e9-c1426baedc3f.PNG)

#### 7. SWOT 분석
![swot](https://user-images.githubusercontent.com/62641007/81142317-531f6480-8faa-11ea-9b18-1aa6e5928ae4.PNG)

#### 8. 
![plan](https://user-images.githubusercontent.com/62641007/81142320-54e92800-8faa-11ea-879e-25c6abceceb8.PNG)
