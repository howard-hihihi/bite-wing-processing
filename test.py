import cv2

# 加載物體檢測模型
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 讀取圖片
img = cv2.imread(r"C:\Users\user\Desktop\dataset\periapical film\Adaptive_Histogram_Equalization\original size\11.jpg",
                 cv2.IMREAD_GRAYSCALE)


# 進行物體檢測
faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)

# 遍歷檢測到的物體
for (x, y, w, h) in faces:
    # 計算物體中心
    center_x = x + w // 2
    center_y = y + h // 2

    # 在圖片上劃出物體邊界框和中心
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.circle(img, (center_x, center_y), 5, (0, 255, 0), -1)

# 顯示結果
cv2.imshow('Object Tracking', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
