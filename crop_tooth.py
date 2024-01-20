import cv2
import os

def save_resize_img(root):
    for name in os.listdir(root):
        img_path = os.path.join(root_dir, name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (width, height))
        print(f"resize image {img_path}")

        cv2.imwrite(img_path, img)

'''
cv2.Laplacian(img, ddepth, ksize, scale)
-- img 來源影像
-- ddepth 影像深度，設定 -1 表示使用圖片原本影像深度
-- ksize 運算區域大小，預設 1 ( 必須是正奇數 )
-- scale 縮放比例常數，預設 1 ( 必須是正奇數 )

cv2.Sobel(img, ddepth, dx, dy, ksize, scale)
-- img 來源影像
-- dx 針對 x 軸抓取邊緣
-- dy 針對 y 軸抓取邊緣
-- ddepth 影像深度，設定 -1 表示使用圖片原本影像深度
-- ksize 運算區域大小，預設 1 ( 必須是正奇數 )
-- scale 縮放比例常數，預設 1 ( 必須是正奇數 )

cv2.Canny(img, threshold1, threshold2, apertureSize)
-- img 來源影像
-- threshold1 門檻值，範圍 0～255
-- threshold2 門檻值，範圍 0～255
-- apertureSize 計算梯度的 kernel size，預設 3
'''
def edge_detect(img):
    img = cv2.GaussianBlur(img, (5, 5), 3)  # 使用高斯濾波器進行模糊
    img = cv2.medianBlur(img, 3)

    # img = cv2.Laplacian(img, -1, 3, 5)        # 偵測邊緣
    # img = cv2.Sobel(img, -1, 1, 3, 5, 7)      # 偵測邊緣
    img = cv2.Canny(img, 50, 31, 23)              # 偵測邊緣

    return img


    

root_dir = "Images"
img_name = "11.jpg"
img_path = os.path.join(root_dir, img_name)
width, height = 640, 640

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = cv2.equalizeHist(img)
img = edge_detect(img)

_, img = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 遍歷每個輪廓
for contour in contours:
    # 獲得輪廓的邊界框
    x, y, w, h = cv2.boundingRect(contour)
    if w * h > 4000:
        # 在原始圖像上劃出矩形
        cv2.rectangle(img, (x, y), (x + w, y + h), 255, 2)

cv2.imshow(img_name, img)
cv2.waitKey()
cv2.destroyAllWindows()