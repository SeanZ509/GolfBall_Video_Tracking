import sys
import cv2
from ultralytics import YOLO

def GolfballDetector(input_video, output_video):
    model_path = 'yolov5s_V2.pt'
    model = YOLO(model=model_path)
    cap = cv2.VideoCapture(input_video)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'MP4V'), fps, (frame_width, frame_height))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    if len(sys.argv) != 2:
        print("Incorrect Args: <Input_Video>")
        sys.exit(1)

    input_video = sys.argv[1]
    output_video = 'golfball_detected_' + input_video

    GolfballDetector(input_video, output_video)

if __name__ == '__main__':
    main()