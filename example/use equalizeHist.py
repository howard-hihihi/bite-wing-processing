import cv2
from matplotlib import pyplot as plt

width, height = 640, 640
image = cv2.imread("dataset/train/images/74_1.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (width, height))
equalize_image = cv2.equalizeHist(image)
guassian_image = cv2.GaussianBlur(equalize_image, ksize=(3, 3), sigmaX=1)


cv2.imshow("img", image)
cv2.imshow("equalize img", equalize_image)
cv2.imshow("guassian img", guassian_image)
cv2.waitKey()
cv2.destroyAllWindows()

 
# plot image histogram
'''
ravel 是 numpy 的一個函數，將多為數組轉為一維
'''
plt.hist(image.ravel(), 256, [0, 255], label= 'original image')
plt.hist(equalize_image.ravel(), 256, [0, 255], label= 'equalize image')
plt.hist(guassian_image.ravel(), 256, [0, 255], label= 'guassian image')
plt.legend()
plt.show()
