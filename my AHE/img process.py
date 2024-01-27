import cv2
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\dataset\periapical film\original images\original size\images\11.jpg", cv2.IMREAD_GRAYSCALE)
height, width = img.shape
cv2.imwrite("output/original_img.jpg", img)

# img = cv2.resize(img, (width//2, height//2))
# height, width = img.shape

# 使用中值濾波器減少噪聲
img = cv2.medianBlur(img, 3)

# 建立CLAHE對象
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

'''----------------------------------------------'''
# 第一次直方圖均質化，分四等分
img_1 = img[:height//2, :width//2]
img_2 = img[:height//2, width//2:]
img_3 = img[height//2:, :width//2]
img_4 = img[height//2:, width//2:]

# 適應性直方圖均衡化
img_1_equalized = clahe.apply(img_1)
img_2_equalized = clahe.apply(img_2)
img_3_equalized = clahe.apply(img_3)
img_4_equalized = clahe.apply(img_4)

# cv2.imshow("img_1", img_1_equalized)
# cv2.imshow("img_2", img_2_equalized)
# cv2.imshow("img_3", img_3_equalized)
# cv2.imshow("img_4", img_4_equalized)

temp_1 = np.concatenate((img_1_equalized, img_2_equalized), axis=1)
temp_2 = np.concatenate((img_3_equalized, img_4_equalized), axis=1)
save_img = np.concatenate((temp_1, temp_2), axis=0)
cv2.imwrite("output/img_025.jpg", save_img) # 0.25

'''----------------------------------------------'''
# 第二次直方圖均質化，1、2合併 3、4合併，分兩等分
img_5 = np.concatenate((img_1_equalized, img_2_equalized), axis=1)
img_6 = np.concatenate((img_3_equalized, img_4_equalized), axis=1)

img_5_equalized = clahe.apply(img_5)
img_6_equalized = clahe.apply(img_6)

# cv2.imshow("img_5", img_5_equalized)
# cv2.imshow("img_6", img_6_equalized)

save_img = np.concatenate((img_5_equalized, img_6_equalized), axis=0)
cv2.imwrite("output/img_050.jpg", save_img) # 0.50

'''----------------------------------------------'''
# 第三次直方圖均質化，5 合併 6 合併，變成一個完整
img_7 = np.concatenate((img_5_equalized, img_6_equalized), axis=0)
img_7_equalized = clahe.apply(img_7)

# cv2.imshow("img_7", img_7_equalized)

save_img = img_7_equalized
cv2.imwrite("output/img_100.jpg", save_img) # 1.00

'''----------------------------------------------'''
new_img = img
average_img = np.clip((new_img.astype(np.uint16) + save_img.astype(np.uint16)) // 2, 0, 255).astype(np.uint8)
cv2.imwrite("output/average_img.jpg", average_img)
'''----------------------------------------------'''
cv2.imshow("average", average_img)
cv2.imshow("img", img)

cv2.waitKey()
cv2.destroyAllWindows()