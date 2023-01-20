import os
import json

# Sample JSON input
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


# Function to create the folder and file structure
def create_structure(json_data, parent_folder):
    for key, value in json_data.items():
        # Check if the key is a file or a folder
        if "." in key:
            # If it's a file, write the content to the file
            file_path = os.path.join(parent_folder, key)
            with open(file_path, "w") as f:
                f.write(value)
        else:
            # If it's a folder, create the folder and recursively call the function
            folder_path = os.path.join(parent_folder, key)
            os.mkdir(folder_path)
            create_structure(value, folder_path)


# Create the root folder
root_folder = "output"
os.mkdir(root_folder)

# Call the function to create the folder and file structure
create_structure(json_input, root_folder)
