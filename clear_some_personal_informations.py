from PIL import Image
import numpy as np

# 读取图片
# img1 = Image.open('陈冠斌_自动驾驶算法.jpg')
image_name = '陈冠斌_自动驾驶算法.jpg'
# image_name = '陈冠斌_C++研发工程师_智驾_地图_Page1.jpg'
img1 = Image.open(image_name)
img = np.array(img1, dtype=np.uint8)
image_name_new = image_name[:-4] + '_auto.jpg'

# 图片处理（覆盖区域）
value = 255  # 填充白色

# img[0:360, 0:1800, :] = value

img[0:210, 0:1800, :] = value
# img[0:250, 0:1800, :] = value


# img[217:255, 0:800, :] = value
# img[63:257, 849:1058, :] = value

# ratio = 1.5
# img[0:int(212*ratio), 0:int(640*ratio), :] = value
# img[int(217*ratio):int(255*ratio), 0:int(800*ratio), :] = value
# img[int(63*ratio):int(257*ratio), int(849*ratio):int(1058*ratio), :] = value

# 转换回PIL图片并保存
img_new = Image.fromarray(img)
img_new.save(image_name_new)

# 用系统默认查看器显示处理后的图片
img_new.show()

# from PIL import Image
# import cv2
# import matplotlib.pyplot as plt    # 显示PIL.Image读取的图片
# import numpy as np

# '''
# image1 = cv2.imread(r'C:/Users/chenguanbin/Latex_Profile_CS_and_OI/陈冠斌_个人简历_2025年6月毕业_CS_Page1.png') 
# print('type(image1):', type(image1))    # type(image1): <class 'numpy.ndarray'>
# print(image1.shape)    # (109, 992, 3)
# print(image1.dtype)    # uint8
# '''

# img1 = Image.open('陈冠斌_个人简历_Page1.jpg')
# # print(type(img1))
# img = np.array(img1, dtype=np.uint8)
# # print(type(img))
# # print(img.shape)

# value = 255 # 0
# ratio=1.42
# img[0:int(212*ratio), 0:int(640*ratio), :] = value
# img[int(217*ratio):int(255*ratio), 0:int(800*ratio), :] = value
# img[int(63*ratio):int(257*ratio), int(849*ratio):int(1058*ratio), :] = value

# img_new = Image.fromarray(img)

# img_new.save('陈冠斌_个人简历_Page1.jpg_auto.jpg')




# '''
# 620
# 209

# 805
# 217-255
# '''