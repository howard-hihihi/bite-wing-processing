import os
import cv2

def change_robo_file_name(label_dir):    
    for old_label_name in os.listdir(label_dir):
        if len(old_label_name.split(".")) == 2: 
            break
        new_label_name = old_label_name.split("_")[0] + ".txt"
        
        old_label_path = os.path.join(label_dir, old_label_name)
        new_label_path = os.path.join(label_dir, new_label_name)
        
        os.rename(old_label_path, new_label_path)

def read_yolo_annotations(annotation_path):
    with open(annotation_path, 'r') as f:
        lines = f.readlines()
    
    annotations = []
    for line in lines:
        data = line.strip().split()
        class_id = int(data[0])
        center_x, center_y, width, height = map(float, data[1:])
        annotations.append({'class_id': class_id, 'center_x': center_x, 'center_y': center_y, 'width': width, 'height': height})
    
    return annotations

def crop_image(image_path, annotations, output_folder):
    image = cv2.imread(image_path)
    image_name = os.path.split(image_path)[1]
    i = 1
    
    for annotation in annotations:
        center_x = int(annotation['center_x'] * image.shape[1])
        center_y = int(annotation['center_y'] * image.shape[0])
        width = int(annotation['width'] * image.shape[1])
        height = int(annotation['height'] * image.shape[0])
        
        x = center_x - width // 2
        y = center_y - height // 2
        
        cropped_image = image[y:y+height, x:x+width]
        
        # 進行你的處理，例如儲存切割後的照片
        output_path = f'{output_folder}/{os.path.splitext(image_name)[0]}_{i}.jpg' # 修改这一行
        i += 1
        cv2.imwrite(output_path, cropped_image)




# 資料夾的路徑
images_folder = 'D:\\Python Project\\dataset\\periapical film\\640 x 640\\images' # change  "images"
labels_folder = 'D:\\Python Project\\dataset\\periapical film\\640 x 640\\labels' # change  "labels/yolo"
output_folder = "D:\\Python Project\\dataset\\periapical film\\640 x 640 crop\\images"

# 這個資料夾的範例
# images_folder = 'images' 
# labels_folder = 'labels/yolo' 
# output_folder = "tooth_crop"

os.makedirs(output_folder, exist_ok=True)

# 更改 roboflow 標記的檔名
change_robo_file_name(labels_folder)

# 讀取每個影像的標註
i = 1
for image_filename in os.listdir(images_folder):
    if image_filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(images_folder, image_filename)
        
        # 構建對應的標註檔案的路徑
        label_filename = os.path.splitext(image_filename)[0] + '.txt'
        label_path = os.path.join(labels_folder, label_filename)
        
        # 檢查標註檔案是否存在
        if os.path.exists(label_path):
            annotations = read_yolo_annotations(label_path)
            crop_image(image_path, annotations, output_folder)
        else:
            print(f"Warning: No label file found for {image_filename}---{i}")
            i += 1
