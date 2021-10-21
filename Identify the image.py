# -*- coding:utf-8 -*-
"""
作者：minieye
日期：2021年月19日
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 高斯滤波
def GausBlur(img):
    gaus = cv2.GaussianBlur(img, (5, 5), 2)  # (5, 5)表示高斯矩阵的长与宽都是5，标准差取2
    return gaus


# 灰度处理
def Gray_img(gaus_img):
    gray = cv2.cvtColor(gaus_img, cv2.COLOR_BGR2GRAY)
    return gray


# 开运算操作
def open_mor(binary):
    kernel = np.ones((6, 6), np.uint8)  # 8 8 数字可以自己改变加以调整效果  数字越大强度越高
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=5)  # iterations进行7次操作  次数越多效果越强
    return opening


# 定义一个图像处理函数
def img_disapose():
    # 捕获存储完图像之后 对图像进行处理
    # 读取上面存储的图片
    img = cv2.imread('cap_RGB.jpg')  # 0为灰度，1为彩色
    img = cv2.resize(img, (640, 480))  # 设置窗口大小
    # 高斯滤波
    gaus_img = GausBlur(img)
    # 灰度处理
    gray_img = Gray_img(gaus_img)
    # 二值化处理
    ret, binary = cv2.threshold(gray_img, 148, 255, cv2.THRESH_BINARY)  # 148  255 为设置阈值
    # 开运算操作
    open_img = open_mor(binary)
    # 颜色反转一下
    open_img = ~open_img
    # 轮廓检测
    contours, hierarchy = cv2.findContours(open_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print('hierarchy', hierarchy)
    # 描绘轮廓
    c = sorted(contours, key=cv2.contourArea, reverse=True)[0]
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    # 重点 这里的img要换成frame
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
    cv2.putText(frame, 'xuebi', (box[0][0], box[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)


cv2.namedWindow("Photo_Detect")  # 定义一个窗口
cap = cv2.VideoCapture(0)  # 捕获摄像头图像  0位默认的摄像头 笔记本的自带摄像头  1为外界摄像头
while (True):  # 值为1不断读取图像
    ret, frame = cap.read()  # 视频捕获帧
    cv2.imwrite('cap_RGB.jpg', frame)  # 写入捕获到的视频帧  命名为cap_RGB.jpg
    img_disapose()  # 图像处理
    cv2.imshow('Photo_Detect', frame)  # 显示窗口 查看实时图像

    if cv2.waitKey(1) & 0xFF == ord('Q'):  # 按Q关闭所有窗口  一次没反应的话就多按几下
        break

# 执行完后释放窗口
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
