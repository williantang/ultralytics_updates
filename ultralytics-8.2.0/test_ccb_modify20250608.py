from ultralytics import  YOLO

yolo = YOLO("runs/detect/train11/weights/best.pt",task="detect")
results = yolo(source="frame3_0568.jpg",show = True)



