import cv2
import numpy as np

def boundary_tracing(image):
    # 將灰階圖片二值化
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("thresh", thresh)

    # 找到輪廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 使用 Moore's Boundary Tracing Algorithm
    boundary_points = []
    for contour in contours:
        for point in contour:
            boundary_points.append(point[0])

    boundary_points = np.array(boundary_points)

    return boundary_points

# 讀取灰階照片
image_path = r'C:\Users\user\Desktop\image processing\tooth\37_jpg.rf.5a5961a0c22de152085aa353d497a25b.jpg'  # 將路徑替換為你的照片路徑
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# gray_image = cv2.resize(gray_image, (gray_image.shape[1]//2, gray_image.shape[0]//2))

# 執行邊界追蹤算法
boundary_points = boundary_tracing(gray_image)

# 在原始圖片上畫出邊界
output_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
cv2.polylines(output_image, [boundary_points], isClosed=True, color=(0, 255, 0), thickness=2)

# 顯示原始圖片和處理後的圖片
cv2.imshow('Original Image', gray_image)
cv2.imshow('Boundary Tracing', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
