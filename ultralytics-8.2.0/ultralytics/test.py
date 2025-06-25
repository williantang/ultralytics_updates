from ultralytics import YOLO
 
if __name__=="__main__":
    
 
    test_path=r"/home/gengyu/ultralytics-8.2.0/ultralytics/assets/bus.jpg"
   
    model = YOLO('yolov8n.pt')  # load an official model
    
 
    # Predict with the model
    results = model(test_path,save=True,conf=0.5)  # predict on an image
