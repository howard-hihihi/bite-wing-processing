import os

path = "C:\\Users\\user\\Desktop\\dataset\\dataset_1\\labels"
file_list = os.listdir(path)

for i in range(len(file_list)):
    if file_list[i][0] == "a":
        old_file = file_list[i]
        new_file = file_list[i][1:]
        old_file_path = os.path.join(path, old_file)
        new_file_path = os.path.join(path, new_file)
        os.rename(old_file_path, new_file_path)
