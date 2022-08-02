import cv2
import imutils
import numpy as np
import datetime

protopath = 'MobileNetSSD_deploy.prototxt'
modelpath = 'MobileNetSSD_deploy.caffemodel'

detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

def main():
    #cap = cv2.VideoCapture('.\data\people.mp4')
    cap = cv2.VideoCapture(0)

    fps = 0
    total_frames = 0
    fps_start_time = datetime.datetime.now()

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame,800)
        total_frames += 1
        

        #detect people
        (H,W) = frame.shape[:2]

        #create a blob out of our image
        blob = cv2.dnn.blobFromImage(frame,  0.007843, (W, H), 127.5)
        detector.setInput(blob)

        person_detections = detector.forward()

        for i in np.arange(0,person_detections.shape[2]):
            confidence =person_detections[0,0,i,2]

            if confidence>0.5:
                index = int(person_detections[0,0,i,1])
                if CLASSES [index] != "person":
                    continue

                person_box = person_detections[0,0,i,3:7] * np.array([W,H,W,H])
                (startX, startY, endX, endY) = person_box.astype("int")

                cv2.rectangle(frame,(startX,startY),(endX,endY),(0,0,255),2)

        #display the fps
        fps_end_time = datetime.datetime.now()
        time_diff = (fps_end_time - fps_start_time).seconds

        if time_diff == 0:
            fps = 0
        else:
            fps = total_frames/time_diff

        fps_text = f'FPS: {fps:.2f}'
        cv2.putText(frame,fps_text,(5,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

        cv2.imshow('frame',frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
# def main():
#     image = cv2.imread('.\data\people.jpg')
#     image = imutils.resize(image,width=800)

#     (H,W) = image.shape[:2]

#     #create a blob out of our image
#     blob = cv2.dnn.blobFromImage(image,  0.007843, (W, H), 127.5)
#     detector.setInput(blob)

#     person_detections = detector.forward()

#     for i in np.arange(0,person_detections.shape[2]):
#         confidence =person_detections[0,0,i,2]

#         if confidence>0.5:
#             index = int(person_detections[0,0,i,1])
#             if CLASSES [index] != "person":
#                 continue

#             person_box = person_detections[0,0,i,3:7] * np.array([W,H,W,H])
#             (startX, startY, endX, endY) = person_box.astype("int")

#             cv2.rectangle(image,(startX,startY),(endX,endY),(0,0,255),2)

#     cv2.imshow("Results", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

if __name__ == '__main__':
    main()