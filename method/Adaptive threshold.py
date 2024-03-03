import cv2
import numpy as np
import os

img_dir = "tooth/APLIT"
output_dir = "tooth/APLIT_adaptive_threshold"

os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, name)
    output_path = os.path.join(output_dir, name)

    # 讀取圖片
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.medianBlur(image, 15)

    '''
    使用自適應閾值處理
    cv2.ADAPTIVE_THRESH_MEAN_C 表示使用鄰域區域的平均值作為閾值
    cv2.THRESH_BINARY 表示二值化操作
    blockSize 指定區域大小，C 指定從平均值中減去的常數
    '''

    adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # # 顯示原始圖片和處理後的圖片
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Adaptive Threshold', adaptive_threshold)

    # # 等待按下任意鍵，然後關閉視窗
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    cv2.imwrite(output_path, adaptive_threshold)