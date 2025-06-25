import cv2
import numpy as np
from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog, scrolledtext
from stata_analy import parse_ascii_binary_with_ff_separator as parse_ascii_binary

def video_analy(video_path):
    # 初始化YOLOv8模型
    mdl = '/home/gengyu/ultralytics-8.2.0/runs/detect/train10/weights/best.pt'
    video_path = video_path
    # 设置自己训练好的模型路径
    model = YOLO(mdl)
    # 读取视频文件
    cap = cv2.VideoCapture(video_path)
    cls_list = []
    boxes_length = []
    # 逐帧进行预测
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 对每一帧进行预测。并设置置信度阈值为0.8，需要其他参数，可直接在后面加
        results = model(frame, False, conf=0.4)
        conf = True
        # 绘制预测结果
        for result in results:
            # 绘制矩形框
            for box in result.boxes:
                xyxy = box.xyxy.squeeze().tolist()
                x1, y1, x2, y2 = int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])
                c, conf, id = int(box.cls), float(box.conf) if conf else None, None if box.id is None else int(
                    box.id.item())
                cls_list.append(c)
                name = ('' if id is None else f'id:{id} ') + result.names[c]
                label = name
                confidence = conf

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (255, 255, 0),
                            2)
        # 或者使用下行代码绘制所有结果
        # res=results[0].plot(conf=False)
        # 显示预测结果
        cv2.namedWindow("Predictions", cv2.WINDOW_NORMAL)
        cv2.imshow("Predictions", frame)
        cv2.resizeWindow("Predictions", 660, 960)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # 释放资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()
    new_list = []
    state_list = []
    for i in range(0, len(cls_list), 2):
        if i + 1 < len(cls_list):
            if cls_list[i] == 2 or cls_list[i + 1] == 2:
                new_list.append(1)
            elif cls_list[i] == "none" or cls_list[i + 1] == "none":
                new_list.append(10)
            else:
                new_list.append(0)
        else:
            # 处理列表长度为奇数时最后一个元素的情况
            if cls_list[i] == 1:
                new_list.append(1)
            else:
                new_list.append(0)
    for i in range(0, len(new_list), 3):
        sublist = new_list[i:i + 3]
        ones = sum(sublist)
        if ones == 3:
            state_list.append(1)
        elif ones == 0 or ones == 1:
            state_list.append(0)
        elif ones == 2:
            state_list.append(1)
        else:
            state_list.append('none')
    return state_list




if __name__ =='__main__':
    result = video_analy('/home/gengyu/ultralytics-8.2.0/8_38400_NONE_1.MOV')
    print(result)
