import cv2
import numpy as np
import os

source = "tooth"
output = "output_images"

for image_name in os.listdir(source):
    output_path = output + "/" + image_name

    # 讀取影像
    image = cv2.imread(source + "/" + image_name, cv2.IMREAD_GRAYSCALE)

    # 使用Sobel算子進行邊緣檢測
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

    # 計算梯度大小
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)

    # 將梯度大小映射到0-255的範圍
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # 將梯度大小轉換為8位元整數型態
    gradient_magnitude = np.uint8(gradient_magnitude)

    cv2.imwrite(output_path, gradient_magnitude)

    # 顯示原始影像和邊緣檢測結果
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Sobel Edge Detection', gradient_magnitude)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
