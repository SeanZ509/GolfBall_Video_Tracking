#Convert Video To Frames - Frames to be annotated - Change video and output path for new videos

import cv2
import os

video_path = 'Training_Videos/trainv8.mp4'

if not os.path.exists(video_path):
    print("Video file not found.")
else:
    print("Video file found.")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
    else:
        print("Video opened successfully.")

        output_folder = 'frames'
        os.makedirs(output_folder, exist_ok=True)

        if os.path.exists(output_folder) and os.access(output_folder, os.W_OK):
            print("Output directory is ready.")
        else:
            print("Error: Output directory not writable.")

        frame_count = 0
        while True:
            success, frame = cap.read()
            if not success:
                print(f"Finished reading frames. Total frames read: {frame_count}")
                break

            frame_path = os.path.join(output_folder, f'v8_frame_{frame_count}.jpg')
            if cv2.imwrite(frame_path, frame):
                print(f"Frame {frame_count} saved.")
            else:
                print(f"Error saving frame {frame_count}.")
            frame_count += 1

        cap.release()