import cv2

img1 = cv2.imread(r"C:\Users\user\Desktop\dataset\periapical film\original images\original size\images\11.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r"C:\Users\user\Desktop\dataset\periapical film\Adaptive_Histogram_Equalization(AHE)\original size\11.jpg", cv2.IMREAD_GRAYSCALE)


img3 = cv2.subtract(img1, img2)
img4 = cv2.subtract(img2, img1)

cv2.imwrite(r"C:\Users\user\Desktop\dataset\periapical film\subtract\11_original_AHE.jpg", img3)
cv2.imwrite(r"C:\Users\user\Desktop\dataset\periapical film\subtract\11_AHE_original.jpg", img4)

# cv2.imshow('image_3', img3)
# cv2.imshow("image_4", img4)
# cv2.waitKey()
# cv2.destroyAllWindows()