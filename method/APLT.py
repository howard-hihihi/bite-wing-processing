import cv2
import numpy as np
import math

def adaptive_power_law_transform(img, window_size):
    p, q = window_size//2, window_size//2
    height, width = img.shape
    result_img = np.zeros_like(img, dtype=np.uint8)

    ## Normalize the image to the range [0, 1]
    normalized_img = img / 255.0
    
    for x in range(p, width - p):
        for y in range(q, height - q):
            w_max = np.max(normalized_img[y-q : y+q+1, x-p : x+p+1])
            w_min = np.min(normalized_img[y-q : y+q+1, x-p : x+p+1])
            d_xy = w_max - w_min
            d_xy = max(d_xy, 1e-10) # 避免 w_max 很接近 w_min
            gamma = math.log(1 / d_xy)
            result_img[y, x] = np.clip((normalized_img[y, x] ** gamma) * 255, 0, 255)

    return result_img

'''---------------------------------------------------------------------------------'''
# window_size = 1
# for i in range(1):
#     # 讀取圖像
#     image = cv2.imread('image_enhancement/images/11_original.jpg', cv2.IMREAD_GRAYSCALE)
#     image = cv2.resize(image, (image.shape[1]//4, image.shape[0]//4))

#     # 設定窗口大小
#     window_size += 6
#     print("window: ", window_size)
#     # 執行自適應冪律轉換
#     aplt_image = adaptive_power_law_transform(image, window_size)
#     cv2.imwrite("image_enhancement/images/11_APLT_ws7.jpg", aplt_image)

#     # 顯示原始和增強後的圖像
#     cv2.imshow('Original Image', image)
#     cv2.imshow('APLT Image', aplt_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
'''---------------------------------------------------------------------------------'''

# 儲存照片
import os

input_dir = "tooth/images"
save_dir = "tooth/APLT"
window_size = 9

os.makedirs(save_dir, exist_ok=True)

i = 0
for img_name in os.listdir(input_dir):
    # if i > 20: break

    img_path = os.path.join(input_dir, img_name)
    save_path = os.path.join(save_dir, img_name)

    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    ## 執行自適應冪律轉換
    aplt_image = adaptive_power_law_transform(image, window_size)

    cv2.imwrite(save_path, aplt_image)
    # print("save: ", save_path)
    i += 1