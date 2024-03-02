import cv2
import numpy as np
import os

img_dir = "tooth/original_sobel"
output_dir = "tooth/original_sobel_OTSU"

os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(img_dir):
   img_path = os.path.join(img_dir, name)
   output_path = os.path.join(output_dir, name)


   # 讀取灰度圖像
   image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
   height, width = image.shape
   image = cv2.resize(image, (int(width*0.5), int(height*0.5)))

   # Otsu's 方法
   '''
   a. image: 輸入的灰度圖像。
   b. 0: 閾值，這裡設置為 0，因為 Otsu's 方法會忽略這個參數。
   c. 255: 超過閾值的像素賦予的新值，這裡設置為 255，表示二值化後的像素值為最大值。
   d. cv2.THRESH_BINARY + cv2.THRESH_OTSU: 這是二值化的方法，
      其中 cv2.THRESH_BINARY 表示超過閾值的像素賦予給新值（在這裡是 255），否則賦予 0，
      而 cv2.THRESH_OTSU 則表示使用 Otsu's 方法自動選擇閾值。
   '''

   _, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

   cv2.imwrite(output_path, otsu_threshold)


   # # 顯示原始圖像和 Otsu's 方法處理後的圖像
   # cv2.imshow('Original Image', image)
   # cv2.imshow('Otsu Threshold', otsu_threshold)

   # # 等待按下任意鍵，然後關閉視窗
   # cv2.waitKey(0)
   # cv2.destroyAllWindows()
