import cv2
import numpy as np
import os

img_dir = "tooth/APLIT_OTSU"
output_dir = "tooth/APLIT_OTSU_erosion"

os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, name)
    output_path = os.path.join(output_dir, name)

    # 讀取二值化的照片
    binary_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 定義圓形的結構元素（這裡使用圓形核心）
    # kernel = np.ones((3, 5), np.uint8) # 矩形
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # 橢圓形
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)) # 十字架

    # 進行腐蝕操作
    erosion = cv2.erode(binary_image, kernel, iterations=1)
    cv2.imwrite(output_path, erosion)

    # 顯示原始二值化影像和腐蝕的結果
    # cv2.imshow('Original Binary Image', binary_image)
    # cv2.imshow('Erosion Result', erosion)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
