import cv2
import numpy as np

def adaptive_power_law_transform(image, alpha, beta, gamma):
    # 將圖像轉為浮點數格式
    img_float = image.astype(np.float32) / 255.0

    # 執行自適應功率法則密度轉換
    transformed_img = np.power(alpha * img_float, gamma) * beta

    # 將值限制在合理範圍內
    transformed_img = np.clip(transformed_img, 0, 1)

    # 將浮點數格式轉為 8 位無符號整數格式
    transformed_img = (transformed_img * 255).astype(np.uint8)

    return transformed_img

# 讀取圖像
image = cv2.imread("image_enhancement/images/34_original.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))

alpha = 0
for i in range(10):
# 設定自適應功率法則的參數
    alpha += 0.2  # 調整參數 
    beta = 1.0  # 調整參數
    gamma = 0.7  # 調整參數
    print(alpha, beta, gamma)

    # 執行自適應功率法則密度轉換
    result_image = adaptive_power_law_transform(image, alpha, beta, gamma)

    # 顯示原始圖像和處理後的圖像
    cv2.imshow('Original Image', image)
    cv2.imshow('Transformed Image', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
