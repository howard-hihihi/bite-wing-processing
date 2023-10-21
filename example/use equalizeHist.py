import cv2
from matplotlib import pyplot as plt

image = cv2.imread("bw_images/34.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (640, 640))
equalize_image = cv2.equalizeHist(image)


cv2.imshow("img", image)
cv2.imshow("equalize img", equalize_image)
cv2.waitKey()
cv2.destroyAllWindows()


# plot image histogram
'''
ravel 是 numpy 的一個函數，將多為數組轉為一維
'''
plt.hist(image.ravel(), 256, [0, 255], label= 'original image')
plt.hist(equalize_image.ravel(), 256, [0, 255], label= 'equalize image')
plt.legend()