import os
import cv2
import numpy as np
import utils    

def piecewise_linear_transform(x):
    y = 0
    if x <= 60 and x >= 0:
        y = (5/6) * x
    elif x <= 180 and x > 60:
        y = (5/4 * x) - 25
    elif x <= 255 and x > 180:
        y = (11/15 * x) + 68
    return y

def grayscale_power_transform(input, r):
    output = (255**(1-r)) * (input**r)
    return output


def center_high(image, x, y):
    width, height = image.shape
    half_width, half_height = (width//2), (height//2)

    if x == half_width and y == half_height:
        return image[y, x]
    x_distance = abs(x-half_width)
    y_distance = abs(y-half_height)
    center_distance = ( half_width**2 + half_height**2 ) ** 0.5

    return image[y, x] * ( center_distance / (x_distance**2 + y_distance**2)**0.5 )
    

def image_processing(image, pts_list):
    for obj_pts in pts_list:
        # max_width, max_height = np.max(obj_pts, axis=0)
        # min_width, min_height = np.min(obj_pts, axis=0)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                value = 0
                if cv2.pointPolygonTest(obj_pts, (x, y), False) > 0:
                    value = grayscale_power_transform(image[y, x], 0.85)
                if value > 255:
                        value = 255
                elif value < 0:
                    value = 0
                image[y, x] = value



old_images_path = "dataset/train/images"
old_labels_path = "dataset/train/labels"
new_images_path = "dataset_b/images"
new_labels_path = "dataset_b/labels"

images_list = os.listdir(old_images_path)
labels_list = os.listdir(old_labels_path)
print(images_list)

for i in range(len(images_list)):
    image_path = os.path.join(old_images_path, images_list[i])
    label_path = os.path.join(old_labels_path, labels_list[i])

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # image = cv2.equalizeHist(image)
    width, height = image.shape

    pts_list = []
    with open(label_path) as file:
        for line in file:
            obj = line.split(" ")
            pts_list.append(obj) # [1, 10, 10, 20] ....
    # print(pts_list) # [[1, 10, 10, 20, 40, 30, 20], [1, 40, 30, 20, 20, 30, 20], ....]

    pts_list = utils.get_pts_list(pts_list, width, height) # [[10 10] [20 40], [30 20]] , .... ]

    image_processing(image, pts_list)  
    
    print("No.", i+1)
    utils.add_modify_image(image, old_images_path, new_images_path, images_list[i], 'b')
    utils.add_modify_label(old_labels_path, new_labels_path, labels_list[i], 'b')

utils.show_two_image("dataset/train/images/a2_1.jpg", "dataset_b/images/b2_1.jpg")    