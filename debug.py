import cv2
import utils

with open("dataset/train/labels/b361_1.txt", 'r') as file:
    pts_list = []
    for line in file:
        pts_list.append(line.split(" "))

pts_list = utils.get_pts_list(pts_list, 640, 640)
print(pts_list[0])