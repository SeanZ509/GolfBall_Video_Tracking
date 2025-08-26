Sean Zahller
5/30/2024
CSCD 585 Deep Learning
Golf Ball Detection Project

Guidelines:
*yoloTorchLoader used to load and save pretrained yolov5 model to work with (yolov5s.pt)
*Utils - createFrames takes a video and saves the frames 30 per second
       - Train_Test_Val SKlearn splitting of the data into yolo format to create the Dataset from
       the images and their corresponding labels
*trainModel - retraining the original yolo model with custom data (Dataset)
*GolfBallDetector - Takes new video and attempts to detect Golf Balls, returns new video in same directory as GolfBallDetector

Image Frame Annotation:
RoboFlow - Very nice tool for annotating and saving images, exported labels in yolo format with the original image.
*Used VGGAnnotator at first and had to restart annotations several times very far in, roboflow allowed for saving and better exports


Yolov5 Model Citation:

preferred-citation:
  type: software
  message: If you use YOLOv5, please cite it as below.
  authors:
  - family-names: Jocher
    given-names: Glenn
    orcid: "https://orcid.org/0000-0001-5950-6979"
  title: "YOLOv5 by Ultralytics"
  version: 7.0
  doi: 10.5281/zenodo.3908559
  date-released: 2020-5-29
  license: AGPL-3.0
  url: "https://github.com/ultralytics/yolov5"
