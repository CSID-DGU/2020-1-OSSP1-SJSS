import time
import serial
from absl import app, flags, logging
from absl.flags import FLAGS
#Tensorflow 에서 제공하는 flags 객체를 사용하면 고정값으로 되어 있는 기본적인 데이터를 편리하게 사용 가능
#flags 객체는 int, float, boolean, string 의 값을 저장하고, 가져다 사용하기 쉽게 해주는 기능
import cv2 #opencv
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs

#DEFINE_*** 로 시작되는 함수를 통해서 key, value 형식과 비슷하게 원하는 데이터를 정의
flags.DEFINE_string('classes', 'C:\\Users\\wnsru\\Desktop\\2020-1-OSSP1-SJSS-4-master\\blocklyduino\\demos\\code\\data\\coco.names', 'path to classes file')
flags.DEFINE_string('weights', 'C:\\Users\\wnsru\\Desktop\\2020-1-OSSP1-SJSS-4-master\\blocklyduino\\demos\\code\\checkpoints\\yolov3.tf',
                    'path to weights file')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('video', './data/video.mp4',
                    'path to video file or number for webcam)')
flags.DEFINE_string('output', None, 'path to output video')
flags.DEFINE_string('output_format', 'XVID', 'codec used in VideoWriter when saving video to file')
flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')
#위와 같이 정의된 값들은 flags.FLAGS 를 통해서 어디에서든지 호출하여 사용 가능


def main(_argv):
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    for physical_device in physical_devices:
        tf.config.experimental.set_memory_growth(physical_device, True)

    if FLAGS.tiny:
        yolo = YoloV3Tiny(classes=FLAGS.num_classes)
    else:
        yolo = YoloV3(classes=FLAGS.num_classes)

    yolo.load_weights(FLAGS.weights)#가중치 파일 로드
    logging.info('weights loaded')#로드 완료 시 확인 용

    class_names = [c.strip() for c in open(FLAGS.classes).readlines()]#classes파일 로드
    logging.info('classes loaded')#로드 완료 시 확인 용

    times = [] #t2-t1다루기 위한 배열

    #cv2.VideoCapture()를 사용해 비디오 캡쳐 객체를 생성
    #안의 숫자는 장치 인덱스(어떤 카메라를 사용할 것인가)를 의미
    #1개만 부착되어 있으면 0, 2개 이상이면 첫 웹캠은 0, 두번째 웹캠은 1으로 지정
    #try:
    #    vid = cv2.VideoCapture(int(FLAGS.video))
    #except:
    #    vid = cv2.VideoCapture(FLAGS.video)

    vid = cv2.VideoCapture(0)
    out = None

    if FLAGS.output:
        # by default VideoCapture returns float instead of int
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))#프레임의 너비
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))#프레임의 높이
        fps = int(vid.get(cv2.CAP_PROP_FPS))#프레임 속도
        #vidowriter 비디오를 저장
        #cv2.VideoWriter(outputFile, fourcc, frame, size) : fourcc는 코덱 정보, frame은 초당 저장될 프레임, size는 저장될 사이즈
        codec = cv2.VideoWriter_fourcc(*FLAGS.output_format)
        out = cv2.VideoWriter(FLAGS.output, codec, fps, (width, height))

    while True:
        _, img = vid.read()

        if img is None:
            logging.warning("Empty Frame")
            time.sleep(0.1)
            #sleep():일정 시간 동안 실행 지연 -> 0.1초 지연
            continue

        img_in = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#(원본이미지, 색상 변환 코드), 이미지의 색상공간을 변경할 수 있음
        #Red, Green, Blue 채널
        
        img_in = tf.expand_dims(img_in, 0) #차원을 추가하여 확장함, img_in이 주어졌을 때, 이 함수는 크기가 1인 차원을 img_in의 구조에서 차원 인덱스(0)에 삽입.
        img_in = transform_images(img_in, FLAGS.size)

        t1 = time.time()#현재 Unix timestamp을 소수로 리턴. 정수부는 초단위이고, 소수부는 마이크로(micro) 초단위
        boxes, scores, classes, nums = yolo.predict(img_in)
        #model.predict(): 훈련 된 모델이 주어지면 새로운 데이터 세트의 레이블을 예측한다. 이 메소드는 새로운 데이터 X_new(예 :) model.predict(X_new)와 같은 하나의 인수를 허용하고 배열의 각 객체에 대해 학습된 레이블을 반환
        t2 = time.time()#현재 Unix timestamp을 소수로 리턴. 정수부는 초단위이고, 소수부는 마이크로(micro) 초단위
        times.append(t2-t1)#배열에 t2-t1값 추가
        times = times[-20:]# times[-20] = *(times-20)

        img = draw_outputs(img, (boxes, scores, classes, nums), class_names)#인식된 박스
         
        if FLAGS.output:
            out.write(img)
        cv2.imshow('output', img)#imshow 는 이미지 보기
        #'output'은 윈도우 창의 제목을 의미하며 img는 cv2.imread() 의 return값 
        if cv2.waitKey(1) == ord('q'):#q 입력 시 종료
            break
        #arduino= serial.Serial('COM3', 9600)
        #for i in range(4):
        #    c = obj[i]
        #    c=c.encode('utf-8')
        #   arduino.write(c)
            
    cv2.destroyAllWindows()
    #화면에 나타난 윈도우를 종료

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
