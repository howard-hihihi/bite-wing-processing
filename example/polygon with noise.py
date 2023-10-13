import cv2
import numpy as np
import random


image = np.zeros((400, 600), dtype=np.uint8)


contours = np.array([[
    [100, 100], [150, 50], [200, 30], [250, 50], [350, 100]
]], dtype=np.int32)
print(contours)


color = (255)  
cv2.fillPoly(image, contours, color)

max_width, max_height = np.max(contours[0], axis=0)
min_width, min_height = np.min(contours[0], axis=0)
print("max_height:", max_height)
print("max_width:", max_width)
print('min_height: ', min_height)
print('min_width: ', min_width)

''' pointPolygonTest
False 第三個參數表示回傳的值是絕對值 , 點到邊的距離
True 點到邊的距離 , 在裡面就是正的 , 在外面就是負的 
'''
for x in range(min_width, max_width, 1):
    for y in range(min_height, max_height, 1):
        if cv2.pointPolygonTest(contours[0], (x, y), True) > 0: 
            noise_color = (random.randint(30, 245))
            image[y, x] = noise_color

image[200, 100] = 255 # 注意是 [y, x]
cv2.circle(image,(100,200),50,color,1)  # 設定 1
cv2.imwrite("output.png", image)  
cv2.imshow("Irregular Polygon with Noise", image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
