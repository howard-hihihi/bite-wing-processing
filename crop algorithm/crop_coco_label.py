import os
import cv2
import numpy as np
import json
from pycocotools.coco import COCO

def extract_polygons(image_path, coco_json_path, output_folder):
    # 讀取影像
    image = cv2.imread(image_path)
    
    # 載入 COCO JSON 檔案
    coco = COCO(coco_json_path)
    
    # 取得所有的標註
    ann_ids = coco.getAnnIds()
    annotations = coco.loadAnns(ann_ids)
    
    # 逐一處理每個標註
    for ann in annotations:
        # 取得多邊形的頂點座標
        segmentation = ann['segmentation'][0]
        
        # 將頂點座標轉換成 NumPy 陣列
        points = np.array(segmentation).reshape((-1, 2)).astype(np.int32)
        
        # 透視變換以提取多邊形區域
        rect = cv2.boundingRect(points)
        roi = image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]

        # 顯示或儲存提取的多邊形區域
        cv2.imshow('Polygon Region', roi)
        cv2.waitKey(0)
        
        # 如果需要儲存，可以使用以下程式碼
        # output_path = f'{output_folder}/polygon_{ann["image_id"]}_{ann["id"]}.jpg'
        # cv2.imwrite(output_path, roi)

    cv2.destroyAllWindows()

# 影像路徑
image_path = 'img.jpg'

# COCO JSON 檔案路徑
coco_json_path = 'coco.json'

# 輸出資料夾（如果需要儲存提取的區域）
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

# 提取多邊形區域
extract_polygons(image_path, coco_json_path, output_folder)
