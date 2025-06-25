from ultralytics import  YOLO

model = YOLO("./yolov8n.pt")

model.train(data="ccb_power.yaml",workers = 1,epochs = 180,batch = 16)
