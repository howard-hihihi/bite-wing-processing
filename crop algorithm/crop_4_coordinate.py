import cv2
import numpy as np

def extract_skewed_rectangle(image_path, pts):
    # 讀取影像
    image = cv2.imread(image_path)
    
    # 將四個點按照左上、右上、右下、左下的順序排列
    pts = np.array(pts, dtype=np.float32)
    
    # 計算透視變換矩陣
    rect_width = max(np.linalg.norm(pts[0] - pts[1]), np.linalg.norm(pts[2] - pts[3]))
    rect_height = max(np.linalg.norm(pts[1] - pts[2]), np.linalg.norm(pts[3] - pts[0]))

    dst_pts = np.array([[0, 0], [rect_width - 1, 0], [rect_width - 1, rect_height - 1], [0, rect_height - 1]], dtype=np.float32)
    M = cv2.getPerspectiveTransform(pts, dst_pts)
    
    # 進行透視變換
    result = cv2.warpPerspective(image, M, (int(rect_width), int(rect_height)))
    
    return result

# 照片路徑
image_path = 'images/11.jpg'

# 四個點的坐標 (左上、右上、右下、左下)
rectangle_pts = [(0, 150), (400, 0), (500, 200), (300, 600)]

# 提取斜的矩形
skewed_rectangle = extract_skewed_rectangle(image_path, rectangle_pts)

# 顯示原始影像和提取的斜的矩形
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Skewed Rectangle', skewed_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
