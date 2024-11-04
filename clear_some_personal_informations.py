from PIL import Image
import cv2
import matplotlib.pyplot as plt    # 显示PIL.Image读取的图片
import numpy as np

'''
image1 = cv2.imread(r'C:/Users/chenguanbin/Latex_Profile_CS_and_OI/陈冠斌_个人简历_2025年6月毕业_CS_Page1.png') 
print('type(image1):', type(image1))    # type(image1): <class 'numpy.ndarray'>
print(image1.shape)    # (109, 992, 3)
print(image1.dtype)    # uint8
'''

img1 = Image.open('陈冠斌_个人简历_2025年6月毕业_CS_Page1.png')
# print(type(img1))
img = np.array(img1, dtype=np.uint8)
print(type(img))
print(img.shape)

value = 255 # 0
img[0:212, 0:620, :] = value
img[217:255, 0:800, :] = value
img[63:257, 849:1058, :] = value

img_new = Image.fromarray(img)

img_new.save('陈冠斌_个人简历_2025年6月毕业_CS_Page1_PS_auto.png')




'''
620
209

805
217-255
'''