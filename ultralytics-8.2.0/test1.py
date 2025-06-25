from ultralytics import  YOLO

yolo = YOLO("runs/detect/train10/weights/best.pt",task="detect")

results = yolo(source='8_38400_NONE_1.MOV',show = True,conf=0.4)
