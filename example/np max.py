import numpy as np

contours = np.array([[
    [100, 100], [150, 50], [200, 30], [250, 50], [300, 100],
    [280, 150], [250, 180], [200, 400], [150, 180], [120, 150]
]], dtype=np.int32)


print(contours)

max_width, max_height = np.max(contours[0], axis=0)
min_width, min_height = np.min(contours[0], axis=0)

# 打印最大长度和宽度
print("max_height:", max_height)
print("max_width:", max_width)
print('min_height: ', min_height)
print('min_width: ', min_width)
