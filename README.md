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
