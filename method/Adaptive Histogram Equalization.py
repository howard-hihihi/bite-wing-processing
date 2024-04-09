"""
"Adaptive Histogram Equalization" (AHE)
"""
import os
import cv2
import matplotlib.pyplot as plt

img_dir = r"C:\Users\user\Desktop\dataset\periapical film\Original Images\101~200"
blur_dir = r"C:\Users\user\Desktop\dataset\periapical film\Median_Blur"
output_dir = "output_images"

os.makedirs(blur_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(img_dir):
    img_path = os.path.join(img_dir, name)
    blur_path = os.path.join(blur_dir, name)
    output_path = os.path.join(output_dir, name)

    # 讀取灰度照片
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 使用中值濾波器減少噪聲
    filtered_image = cv2.medianBlur(img, 5)

    # 建立CLAHE對象
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # 適應性直方圖均衡化
    clahe_img = clahe.apply(filtered_image)

    cv2.imwrite(blur_path, filtered_image)
    # cv2.imwrite(output_path, clahe_img)
    # print(f'save image "{output_path}"')

    # # 顯示原始與增強後的影像
    # plt.figure(figsize=(10, 6))
    # plt.subplot(1, 3, 1)
    # plt.imshow(img, cmap='gray')
    # plt.title('Original Image')

    # plt.subplot(1, 3, 2)
    # plt.imshow(img, cmap='gray')
    # plt.title('medianBlur Image')

    # plt.subplot(1, 3, 3)
    # plt.imshow(clahe_img, cmap='gray')
    # plt.title('CLAHE Image')

    # plt.show()
