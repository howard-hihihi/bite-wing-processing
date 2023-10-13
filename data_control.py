import os
import cv2


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
        images_list = sorted(images_list, key=lambda x: int(x.split("_")[0])) # x 代表 images_list 的 elements
        labels_list = sorted(labels_list, key=lambda x: int(x.split("_")[0]))

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

def add_modify_image(image, folder_path, image_name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    image_path = os.path.join(folder_path, image_name)
    if os.path.exists(image_path):
        name, ext = os.path.splitext(image_name)
        name = name.split('_')[0]
        new_name = f'{name}_12{ext}'
        new_image_path = os.path.join(folder_path, new_name)
        cv2.imwrite(new_image_path, image)
        print("new_name: ", new_name)
    else:
        print(f'**** Did not find original image "{image_name}"')
        



if __name__ == "__main__":
    data_path = "dataset"
    change_name(data_path)
    