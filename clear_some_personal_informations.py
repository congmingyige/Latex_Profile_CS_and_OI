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
# print(type(img))
# print(img.shape)

value = 255 # 0
ratio=1.42
img[0:int(212*ratio), 0:int(640*ratio), :] = value
img[int(217*ratio):int(255*ratio), 0:int(800*ratio), :] = value
img[int(63*ratio):int(257*ratio), int(849*ratio):int(1058*ratio), :] = value

img_new = Image.fromarray(img)

img_new.save('陈冠斌_个人简历_2025年6月毕业_CS_Page1_PS_auto.png')




'''
620
209

805
217-255
'''