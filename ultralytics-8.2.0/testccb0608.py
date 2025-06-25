from ultralytics import  YOLO
import torch.serialization

# 在加载模型之前添加安全全局对象
torch.serialization.add_safe_globals([ultralytics.nn.tasks.DetectionModel])

yolo = YOLO("runs/detect/train11/weights/best.pt",task="detect")
results = yolo(source="frame3_0568.jpg",show = True)



