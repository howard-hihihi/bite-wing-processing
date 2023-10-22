import os
import cv2
import numpy as np
import shutil

def change_name(root):
    data_path = root

    train_image_path = os.path.join(data_path, 'train', 'images')
    valid_iamge_path = os.path.join(data_path, 'valid', 'images')
    test_image_path = os.path.join(data_path, 'test', 'images')
    train_label_path = os.path.join(data_path, 'train', 'labels')
    valid_label_path = os.path.join(data_path, 'valid', 'labels')
    test_label_path = os.path.join(data_path, 'test', 'labels')

    images_path_list = [train_image_path, valid_iamge_path, test_image_path]
    labels_path_list = [train_label_path, valid_label_path, test_label_path]

    '''sort & sorted
    sort 跟 sorted 的差別在於
    sort 直接更改 list 的值 , 不會回傳一個 list , 只能用在 list
    sorted 不直接更改 list , 會回傳一個 list , 可用在多個 data structure
    '''
    for i in range(3):
        images_list = os.listdir(images_path_list[i])
        labels_list = os.listdir(labels_path_list[i])
        # images_list.sort(key=lambda x: int(x.split("_")[0]))
        # labels_list.sort(key=lambda x: int(x.split("_")[0]))
        # images_list = sorted(images_list, key=lambda x: int(x.split("_")[0])) # x 代表 images_list 的 elements
        # labels_list = sorted(labels_list, key=lambda x: int(x.split("_")[0]))


        for j in range(len(images_list)):
            k = 1
            image_name, image_ext = os.path.splitext(images_list[j])
            label_name, label_ext = os.path.splitext(labels_list[j])
            if image_name != label_name:
                print("**** image_name != label_nmae ****")
                break
            else:
                new_image_name = image_name.split("_")[0] + f"_{k}" + image_ext
                new_label_name = label_name.split("_")[0] + f"_{k}" + label_ext
                # while new_image_name in images_list:
                #     new_image_name = new_image_name.split("_")[0] + f"_{k+1}" + image_ext
                #     new_label_name = new_label_name.split("_")[0] + f"_{k+1}" + label_ext
                old_image_path = os.path.join(images_path_list[i], images_list[j])
                old_label_path = os.path.join(labels_path_list[i], labels_list[j])
                new_image_path = os.path.join(images_path_list[i], new_image_name)
                new_label_path = os.path.join(labels_path_list[i], new_label_name)
                os.rename(old_image_path, new_image_path)
                os.rename(old_label_path, new_label_path)
                print(images_list[j], '  ----> ', new_image_name)

def add_modify_image(image, folder_path, image_name, t):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    image_path = os.path.join(folder_path, image_name)
    if os.path.exists(image_path):
        # os.remove(image_path)
        if image_name[0] != t:
            image_name = t + image_name
        name, ext = os.path.splitext(image_name)
        name = name.split('_')[0]
        new_name = f'{name}_1{ext}'
        new_image_path = os.path.join(folder_path, new_name)
        cv2.imwrite(new_image_path, image)
        print("new_name: ", new_name)
    else:
        print(f'**** Did not find original image "{image_name}"')

# 將所有 image、label 複製一份
# shutil.copy("要複製的檔名", "要複製到的路徑")
# shutil.copy("要複製的黨名路徑", "要貼上的路徑")
def add_modify_label(folder_path, label_name, t):
    old_label_path = os.path.join(folder_path, label_name)
    if os.path.exists(old_label_path):
        if label_name[0] != t:
            label_name = t + label_name
        new_label_name = f'{label_name.split("_")[0]}_1.txt'
        new_label_path = os.path.join(folder_path, new_label_name)
        # os.rename(old_label_path, new_label_path)
        shutil.copy(old_label_path, new_label_path)



# 獲取多邊形的各個點，轉成 <class 'numpy.ndarray'>
def get_pts_list(pts, width, height):
    pts_list = []
    for i in range(len(pts)):
        obj_pts = pts[i]
        for j in range(1, len(obj_pts), 2): # 因為 index = 0 , 是類別不是點的座標 , 所以從 index = 1
            x, y = float(obj_pts[j]) * width, float(obj_pts[j+1]) * height
            pts_list.append([x, y])

    pts_list = np.array(pts_list, dtype=np.int32) # 這邊需要轉換成 <class 'numpy.ndarray'>
    return pts_list

if __name__ == "__main__":
    # data_path = "dataset"
    # change_name(data_path)
    '''===================================================='''
    # images_list = os.listdir("temp/images")
    # labels_list = os.listdir("temp/labels")
    # for file in labels_list:
    #     add_modify_label("temp/labels", file, 'b')
    # labels_list = os.listdir("temp/labels")
    # for file in images_list:
    #     image = cv2.imread(os.path.join("temp/images", file))
    #     add_modify_image(image, "temp/images", file, 'b')
    '''===================================================='''