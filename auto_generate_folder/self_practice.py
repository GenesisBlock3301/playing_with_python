import os

json_input = {
    "folder1": {
        "file1.txt": "This is file 1",
        "file2.csv": "Name,Age,Gender\nJohn,25,Male\nJane,30,Female",
        "folder2": {
            "file3.txt": "This is file 3",
            "file4.jpg": "binary data for file 4",
            "folder3": {}
        },
    }
}
current_directory = os.getcwd()


def create_folder(data, current_dir):
    for key, value in data.items():
        print(key, value)
        if "." in key:
            file_path = os.path.join(current_dir, key)
            with open(file_path, 'w') as file:
                file.write(value)
        else:
            folder_path = os.path.join(current_dir, key)
            os.makedirs(folder_path)
            create_folder(value, folder_path)


dic = dict()


def add_to_dic(curr_dir, item):
    if dic.get(os.path.basename(curr_dir), None) and isinstance(dic.get(os.path.basename(curr_dir), None),
                                                                list):
        dic[os.path.basename(curr_dir)].append(item)
    else:
        dic[os.path.basename(curr_dir)] = list()
        dic[os.path.basename(curr_dir)].append(item)


def read_folder_all_child(curr_dir):
    current_folder_files = os.listdir(curr_dir)
    for item in current_folder_files:
        if "." in item:
            add_to_dic(curr_dir, item)
        else:
            directory = os.path.join(curr_dir, item)
            add_to_dic(curr_dir, item)
            read_folder_all_child(directory)


read_folder_all_child(current_directory)
print(dic)
# create_folder(json_input, current_directory)
