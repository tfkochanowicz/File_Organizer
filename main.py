# This project is meant to take all the files in your downloads folder
# and organizes it into folders with catergories such as audio, videos, images etc.
# Look at the code below this comment for the categories files are organized into
# I wrote this project by following the guide here:
# https://blog.mukundmadhav.com/organize-downloads-folder-python-83baf34a05db
# Additionally you could create a .bat or .sh script to automatically after a given
# time interval

import os
from pathlib import Path

folder_names = {
    "Audio": {'aif', 'cda', 'mid', 'midi', 'mp3', 'ogg', 'wav', 'wma'},
    "Compressed": {'7z', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip'},
    'Code': {'js', 'jsp', 'html', 'ipynb', 'py', 'java', 'css'},
    'Documents': {'ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'doc', 'docx', 'txt', 'tex', 'epub'},
    'Images': {'bmp', 'gif', 'jpeg', 'jpg', 'png', 'jfif', 'svg', 'tif', 'tiff'},
    'Softwares': {'apk', 'bat', 'bin', 'exe', 'jar', 'msi', 'py', 'sh'},
    'Videos': {'3gp', 'avi', 'h264', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'wmv'},
    'Others': {'NONE'}
}
# Enter your download path(or whichever folder you want to organize) within the quotes for example:
# downloads_path = r"C:\Users\Me\Downloads"

downloads_path = r""#insert file path here

def new_path(old_path):
    extension = str(old_path).split('.')[-1]
    amplified_folder = extension_filetype_map[extension] if extension in extension_filetype_map.keys() else 'Others'
    final_path = os.path.join(downloads_path, amplified_folder, str(old_path).split('\\')[-1])
    return final_path


# Separate folders and files
onlyfiles = [os.path.join(downloads_path, file)
             for file in os.listdir(downloads_path)
                 if os.path.isfile(os.path.join(downloads_path, file))]

# same as above except if it is not a file it, it must be a folder(look at the if statement)
onlyfolders = [os.path.join(downloads_path, file)
             for file in os.listdir(downloads_path)
                 if not os.path.isfile(os.path.join(downloads_path, file))]


extension_filetype_map = {extension: fileType
        for fileType, extensions in folder_names.items()
            for extension in extensions }

folder_paths = [os.path.join(downloads_path, folder_name)
        for folder_name in folder_names.keys()]

[os.mkdir(folderPath)
        for folderPath in folder_paths if not os.path.exists(folderPath)]


# move files to their location using new_path function
# and create new paths
[Path(eachfile).rename(new_path(eachfile)) for eachfile in onlyfiles]

#move unknown folders
[Path(onlyfolder).rename(os.path.join(downloads_path, 'Others', str(onlyfolder).split('\\')[-1]))
        for onlyfolder in onlyfolders
            if str(onlyfolder).split('\\')[-1] not in folder_names.keys()]


