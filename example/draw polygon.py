import cv2
import numpy as np
import os
import utils

# 把 bite wing 部分變暗
def remove_bw(image, pts_list):
    '''
    cv2.polylines(img, pts, isClosed, color, thickness)
    # img 來源影像
    # pts 座標陣列 ( 使用 numpy 陣列 )
    # isClosed 多邊形是否閉合 , True 閉合 , False 不閉合
    # color 線條顏色，使用 BGR
    # thickness 線條粗細，預設 1
    '''
    # 畫出多邊形
    # cv2.fillPoly(image, [pt_list], 250)
    # cv2.polylines(image, [pt_list], True, 0, 1)

    # 改變像素值
    max_width, max_height = np.max(pts_list, axis=0)
    min_width, min_height = np.min(pts_list, axis=0)
    for x in range(min_width, max_width, 1):
        for y in range(min_height, max_height, 1):
            if cv2.pointPolygonTest(pts_list, (x, y), True) > 0:
                    image[y, x] *= 0.2

# 讀取 images、labels
train_images_path = "dataset/train/images"
train_labels_path = "dataset/train/labels"
# train_images_list = sorted(os.listdir(train_images_path), key=lambda x: int(x.split("_")[0]))
# train_labels_list = sorted(os.listdir(train_labels_path), key=lambda x: int(x.split("_")[0]))
train_images_list = os.listdir(train_images_path)
train_labels_list = os.listdir(train_labels_path)
print(train_images_list, train_labels_list)


for i in range(len(train_images_list)):
    image_path = os.path.join(train_images_path, train_images_list[i])
    label_path = os.path.join(train_labels_path, train_labels_list[i])
    image_1 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # 原圖
    image_2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # 要修改的圖
    image_width, image_height = image_1.shape

    with open(label_path) as file:
        pts_list = []
        for line in file:
            instance_label = line.split(" ") # 物件標記的每個點
            pts_list.append(instance_label)
    
    pts_list = utils.get_pts_list(pts_list, image_width, image_height)

    remove_bw(image_2, pts_list)

    utils.add_modify_image(image_2, train_images_path, train_images_list[i], 'a')
    utils.add_modify_label(train_labels_path, train_labels_list[i]) 


    # 顯示照片
    # cv2.imshow('original', image_1)
    # cv2.imshow('modify', image_2)
    # cv2.waitKey()
    # cv2.destroyAllWindows()