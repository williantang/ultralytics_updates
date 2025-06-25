from ultralytics import  YOLO
import torch
#model define and move to cpu
device = torch.device("cpu")
model = YOLO("./yolov8n.pt")
model = model.to(device)
#train config
model.train(data="ccb_power.yaml",workers = 1,epochs = 180,batch = 16)
