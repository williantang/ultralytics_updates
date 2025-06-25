import tkinter as tk
from tkinter import filedialog, scrolledtext
from stata_analy import parse_ascii_binary_with_ff_separator as parse_ascii_binary
from video_analy import video_analy as va

path = '/home/gengyu/ultralytics-8.2.0/8_38400_NONE_1.MOV'

result = va(path)

print(result)