import cv2
import os

img_dir_1 = "tooth/images"
img_dir_2 = "tooth/APLT"
output_dir = "tooth/subtract/original_APLT"

os.makedirs(output_dir, exist_ok=True)

for name in os.listdir(img_dir_1):
    img_path_1 = os.path.join(img_dir_1, name)
    img_path_2 = os.path.join(img_dir_2, name)
    output_path = os.path.join(output_dir, name)

    img1 = cv2.imread(img_path_1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_path_2, cv2.IMREAD_GRAYSCALE)


    img3 = cv2.subtract(img1, img2)

    cv2.imwrite(output_path, img3)

# cv2.imshow('image_3', img3)
# cv2.imshow("image_4", img4)
# cv2.waitKey()
# cv2.destroyAllWindows()