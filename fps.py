import cv2
import datetime
import imutils

def main():
    cap = cv2.VideoCapture('.\images\Demo.mp4')

    fps = 0
    total_frames = 0
    fps_start_time = datetime.datetime.now()

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame,800)
        total_frames += 1
        
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

if __name__ == '__main__':
    main()

