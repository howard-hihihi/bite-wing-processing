import cv2

image = cv2.imread("dataset/train/images/a2_1.jpg", cv2.IMREAD_GRAYSCALE)
width, height = image.shape

for x in range(width-1):
    for y in range(height-1):
        if x == 320 and y == 320:
            continue
        x_distance = abs(x-320)
        y_distance = abs(y-320)
        center_distance = ( (width/2)**2 + (height/2)**2 ) ** 0.5

        value = image[y, x] * ( center_distance / (x_distance**2 + y_distance**2)**0.5 )
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        image[y, x] = value


cv2.imshow("test_1", image)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("test_1.jpg", image)
