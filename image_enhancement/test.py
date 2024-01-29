import cv2
import numpy as np
import math
from scipy import integrate
import os

def u_function(s, s_up, s_low):
    if s < s_low:
        return 0
    elif s_low <= s <= s_up:
        return 1 / (s_up - s_low)
    else:
        return 0

def cal_mu_1_4(s_up, s_low, s_mean):
    integral_1_4, _ = integrate.quad(lambda s: s / u_function(s, s_up, s_low), s_low, s_mean)
    mu_1_4 = integral_1_4 / integrate.quad(lambda s: u_function(s, s_up, s_low), 0, s_mean)[0]
    return mu_1_4

def cal_mu_3_4(s_up, s_low, s_mean):
    integral_3_4, _ = integrate.quad(lambda s: s / u_function(s, s_up, s_low), s_mean, s_up)
    mu_3_4 = integral_3_4 / integrate.quad(lambda s: u_function(s, s_up, s_low), s_mean, s_up)[0]
    return mu_3_4

def aplit_helper(image, gamma, phi, beta):
    # 進行自適應功率法則密度轉換
    transformed_img = (beta + 1) * np.power(image, gamma) - beta * np.power(image, phi)

    # 將值限制在合理範圍內
    transformed_img = np.clip(transformed_img, 0, 1)

    # 將浮點數格式轉換為 8 位無符號整數格式
    transformed_img = (transformed_img * 255).astype(np.uint8)

    return transformed_img

def aplit(image):
    # 正規化像素值 (S~)
    normalized_image = image / 255.0

    # 計算平均值 (S~)mean
    s_mean = np.mean(normalized_image)
    # print("--> Normalized image mean_value(s_mean): ", s_mean)

    # 設置 F(s) 的參數
    t_thr = 0.5
    s_thr = s_mean * 1.0
    s_up = np.max(normalized_image)
    s_low = np.min(normalized_image)

    # 計算 mu_1/4
    mu_1_4 = cal_mu_1_4(s_up, s_low, s_mean)

    # 計算 mu_3/4
    mu_3_4 = cal_mu_3_4(s_up, s_low, s_mean)

    gamma = math.log(1/4) / math.log(mu_1_4)
    phi = math.log(3/4) / math.log(mu_3_4)
    beta = (t_thr - s_thr**gamma) / (s_thr**gamma - s_thr**phi)
    # print(f'gamma: {gamma}, phi: {phi}, beta: {beta}')

    # APLIT
    aplit_image = aplit_helper(normalized_image, gamma, phi, beta)

    return aplit_image

'''----------------------------------------------------------------------------------------'''
image = cv2.imread("image_enhancement/images/11_AHE.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))
aplit_image = aplit(image)

# (t_thr, s_thr) = (0.5, 1) = (0.3, s_mean * 1.0)
cv2.imwrite("image_enhancement/images/11_AHE_APLIT(0.5, 1).jpg", aplit_image)
cv2.imshow("APLIT", aplit_image)
cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
'''----------------------------------------------------------------------------------------'''
# original size (t_thr, s_thr)
# save_dir = "C:\\Users\\user\\Desktop\\dataset\\periapical film\\AHE_APLIT\\original size"
# input_dir = "C:\\Users\\user\\Desktop\\dataset\\periapical film\\original images\\original size\\images"
# os.makedirs(save_dir, exist_ok=True)

# for img_name in os.listdir(input_dir):
#     img_path = os.path.join(input_dir, img_name)
#     save_path = os.path.join(save_dir, img_name)
#     img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

#     aplit_img = aplit(img)

#     cv2.imwrite(save_path, aplit_img)
#     print("save", save_path)