'''
A self-adaptive image enhancing method based on grayscale power transformation
'''

import cv2
from matplotlib import pyplot as plt
import statistics
import os
import utils

def grayscale_power_transform(input, r):
    output = (255**(1-r)) * (input**r)
    return output

def image_enhance(image):
    # step a : Find average maximum and minimum grayscale aver, max, min of the whole image.
    sorted_value_list = sorted(image.ravel())
    max_val = max(sorted_value_list)
    min_val = min(sorted_value_list)
    mean_val = statistics.mean(sorted_value_list)
    # print("min value: ", max_val)
    print("mean value: ", mean_val)
    # print("min value: ", min_val)



    # step b : Divide grayscale to N (as (3) shown) levels: G[i](i∈[1,N]) between range: [min max].
    difference = max_val - min_val
    if difference > 200:
        N = 16
    elif difference >= 55 and difference <= 200:
        N = 8
    elif difference < 55:
        N = 4
    print("N : ", N)

    # step c : Calculate amount of pixels of each grayscale level: num[i](i∈[1,N]) ·
    hist, bins, _ = plt.hist(sorted_value_list, N, [0, 255], label = "image")# hist 是一個 tuple
    # plt.legend()
    # plt.show()
    # print("hist_b: ", hist_b) # hist_b: [29259. 25041. 20051. 11494.  9140.  ...... 12791. 26801.] 16個值
    # print("bins_b: ", bins_b) # bins_b: [ 0.  15.9375  31.875  47.8125 ...... 223.125  239.0625  255.  ] 17個值

    # stemp d : Find the level containing the most and least pixels G_MAX and G_MIN respectively.
    G_MIN_INDEX = min(hist)
    G_MAX_INDEX = max(hist)
    G_MIN_LEVEL = list(hist).index(G_MIN_INDEX)
    G_MAX_LEVEL = list(hist).index(G_MAX_INDEX)
    # print(f"G_MIN : {bins[G_MIN_LEVEL]} ~ {bins[G_MIN_LEVEL+1]} , pixel數目 : {G_MIN_INDEX}")
    # print(f"G_MAX : {bins[G_MAX_LEVEL]} ~ {bins[G_MAX_LEVEL+1]}, pixel數目 : {G_MAX_INDEX}")

    # step e : Record grayscale "G_LEA" which has the least pixel amount in grayscale level "G_MAX" 
    #          and "G_MOS" which has the most pixel amount in grayscale level "G_MIN"
    G_MOS = 0
    G_LEA = 255
    for pixel in sorted_value_list:
        if pixel >= bins[G_MIN_LEVEL] and pixel < bins[G_MIN_LEVEL+1]:
            G_MOS = max(G_MOS, pixel)
        elif pixel >= bins[G_MAX_LEVEL] and pixel < bins[G_MAX_LEVEL+1]:
            G_LEA = min(G_LEA, pixel)

    # step f : Obtain power transformation coefficient by formula
    r = (3 * mean_val) / (G_MOS + G_LEA)
    # print("r: ", r)

    # step g : Processing image
    width, height = image.shape
    for x in range(width):
        for y in range(height):
            image[y, x] = grayscale_power_transform(image[y, x], r)



# step 0 : Read images
old_images_path = "C:\\Users\\user\\Desktop\\dataset\\dataset_c\\images"
new_images_path = "C:\\Users\\user\\Desktop\\dataset\\dataset_d\\images"
old_labels_path = "C:\\Users\\user\\Desktop\\dataset\\dataset_c\\labels"
new_labels_path = "C:\\Users\\user\\Desktop\\dataset\\dataset_d\\labels"
images_list = os.listdir(old_images_path)
labels_list = os.listdir(old_labels_path)

for i in range(len(images_list)):
    print(f"No.{i+1}: ")
    img_path = os.path.join(old_images_path, images_list[i])
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    image_enhance(img)

    utils.add_modify_image(img, old_images_path, new_images_path, images_list[i], "d")
    utils.add_modify_label(old_labels_path, new_labels_path, labels_list[i], "d")