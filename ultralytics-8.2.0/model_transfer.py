from ultralytics import  YOLO

yolo = YOLO("runs/detect/train9/weights/best.pt",task="detect")

results = yolo(source="/home/gengyu/ultralytics-8.2.0/commun.mp4",show = True)
