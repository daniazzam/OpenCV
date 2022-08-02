cap = cv2.VideoCapture('.\images\Demo.mp4')

fps = 0
total_frames = 0
fps_start_time = datetime.datetime.now()

while True:
    ret, frame = cap.read()
    print(ret)
    frame = imutils.resize(frame,800)
    total_frames += 1
    
    fps_end_time = datetime.datetime.now()
    time_diff = (fps_end_time - fps_start_time).seconds

    fps = total_frames/time_diff

    fps_text = f'FPS: {fps:.2f}'
    print(fps_text)