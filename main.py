import os
import shutil

desktop = 'C:/Users/Sonsi/Desktop/'

directories = {
    'Picture_Sort': ['.jpg', '.png', '.webp', '.jpeg', '.svg', '.JPG', '.PNG'],
    'Music_Sort': ['.mp3', '.wav', '.ogg'],
    'Video_Sort': ['.mp4'],
    'Text_Sort': ['.txt', '.pdf'],
    'File_Sort' : ['.xlsx', '.pptx', '.docx', '.csv', '.doc', '.ppt'],
    'Script_Sort': ['.py', '.ipynb']
}

# ipynb is for capstone, .pbd is for pymol

def fileOrganization():
    for directory, file_types in directories.items():
        file_directory = os.path.join(desktop, directory)
        # check for file existence, if not make one
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
            print("Created directory:", file_directory)
        # sorting the files, by moving them from locaiton to another
        for file_name in os.listdir(desktop):
            if any(file_name.endswith(file_type) for file_type in file_types):
                shutil.move(os.path.join(desktop, file_name), os.path.join(file_directory, file_name))
                print("Moved", file_name, "to", file_directory)

fileOrganization()
