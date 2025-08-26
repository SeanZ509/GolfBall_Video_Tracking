#Original Yolo model loader yolov5s.pt - with orginal detection on test video

import torch
import cv2
from pathlib import Path

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

video_path = 'test.mp4'  
output_path = 'runs/original/test_video_results_iter0.mp4'  
cap = cv2.VideoCapture(video_path)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    results.render()
    frame_with_boxes = results.ims[0]
    out.write(frame_with_boxes)

cap.release()
out.release()
cv2.destroyAllWindows()

