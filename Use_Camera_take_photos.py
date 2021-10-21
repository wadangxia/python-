# -*- coding:utf-8 -*-
"""
作者：minieye
日期：2021年月19日
"""
import cv2
# 采用opencv的库函数去调用摄像头
import datetime  # 或者time

cap = cv2.VideoCapture(0)  # 打开相机
# cv2.VideoCapture(0)代表调取摄像头资源，其中0代表电脑摄像头，1代表外接摄像头(usb摄像头)

video_old_name = datetime.datetime.now()
video_name = str(video_old_name).replace("-", ':')
video_name = video_name.split('.')[0]
video_new_name = video_name + '.' + 'avi'

print("保存视频文件名为：", video_new_name)
print("提示：请按q键结束视频保存")

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter(video_new_name, fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()  # 捕获一帧的图像
    out.write(frame)  # 保存帧
    cv2.imshow('frame', frame)  # 显示帧
    # 判断按键是否为q退出
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()  # 关闭摄像机
out.release()
cv2.destroyWindow(winname=1)  # 关闭窗口
