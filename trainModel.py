from ultralytics import YOLO

def main():
    # Load hyperparameters and options
    model = YOLO(model = 'yolov5s.pt')
    model.train(epochs = 10, batch = 16, val = True,  data='Dataset/data.yaml')
    model.eval()
    model.save('yolov5s_V2.pt')

if __name__ == '__main__':
    main()