import cv2
import matplotlib.pyplot as plt
import os

for name in os.listdir("images"):
    img_path = os.path.join("images", name)
    
    # 讀取四張照片
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape  # 修正顺序

    # 創建一個包含四個子圖的畫布
    fig, axs = plt.subplots(2, 2, gridspec_kw={'wspace': 0.1, 'hspace': 0.1})

    axs[0, 0].imshow(img[:height//2, :width//2], cmap='gray')
    axs[0, 0].axis('off')  # 關閉坐標軸
    axs[0, 1].imshow(img[:height//2, width//2:], cmap='gray')
    axs[0, 1].axis('off')
    axs[1, 0].imshow(img[height//2:, :width//2], cmap='gray')
    axs[1, 0].axis('off')
    axs[1, 1].imshow(img[height//2:, width//2:], cmap='gray')
    axs[1, 1].axis('off')

    # 調整佈局，確保子圖之間的間距合適
    plt.tight_layout()

    # 顯示畫布
    plt.show()
