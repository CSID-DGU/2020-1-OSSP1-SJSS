import time
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
flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
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
    try:
        vid = cv2.VideoCapture(int(FLAGS.video))
    except:
        vid = cv2.VideoCapture(FLAGS.video)

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
            continue

        img_in = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_in = tf.expand_dims(img_in, 0)
        img_in = transform_images(img_in, FLAGS.size)

        t1 = time.time()
        boxes, scores, classes, nums = yolo.predict(img_in)
        t2 = time.time()
        times.append(t2-t1)
        times = times[-20:]

        img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
        img = cv2.putText(img, "Time: {:.2f}ms".format(sum(times)/len(times)*1000), (0, 30),
                          cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
        if FLAGS.output:
            out.write(img)
        cv2.imshow('output', img)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
