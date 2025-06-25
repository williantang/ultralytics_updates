from ultralytics import  YOLO

model = YOLO("./yolov8n.pt")

model.train(data="communication.yaml",workers = 1,epochs = 200,batch = 16)
