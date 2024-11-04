from PIL import Image
import cv2
import matplotlib.pyplot as plt    # 显示PIL.Image读取的图片

image1 = cv2.imread('陈冠斌_个人简历_2025年6月毕业_CS_Page1.png') 
print('type(image1):', type(image1))    # type(image1): <class 'numpy.ndarray'>
print(image1.shape)    # (109, 992, 3)
print(image1.dtype)    # uint8
