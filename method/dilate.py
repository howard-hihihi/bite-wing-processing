import os
import cv2
import numpy as np


img_dir = "tooth/APLIT_OTSU_erosion"
output_dir = "tooth/APLIT_OTSU_erosion_dilate"

os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, name)
    output_path = os.path.join(output_dir, name)

    # 讀取二值化的照片
    binary_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 定義不同形狀的結構元素
    # kernel_rect = np.ones((3, 5), np.uint8)
    # kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    # 進行膨脹操作，分別使用不同形狀的結構元素
    # dilation = cv2.dilate(binary_image, kernel_rect, iterations=1)
    # dilation = cv2.dilate(binary_image, kernel_ellipse, iterations=1)
    dilation = cv2.dilate(binary_image, kernel_cross, iterations=1)

    cv2.imwrite(output_path, dilation)

    # 顯示原始二值化影像和膨脹的結果（使用不同形狀的結構元素）
    # cv2.imshow('Original Binary Image', binary_image)
    # cv2.imshow('Dilation with Rectangular Kernel', dilation_rect)
    # cv2.imshow('Dilation with Elliptical Kernel', dilation_ellipse)
    # cv2.imshow('Dilation with Cross-shaped Kernel', dilation_cross)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
