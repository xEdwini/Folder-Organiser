import os 
import shutil


#D:\PYTHON PROJECTS\pythonLearn\Messy Folder
which_folder = input("Enter the folder path to organise: ")

check_folder = os.path.exists(which_folder)
if not check_folder:
    print("The specified folder does not exist.")
    exit()

files = os.listdir(which_folder)

#File type dictionary to define categories
file_type = {
    "Images" : ["jpg", "jpeg", "png", "gif", "bmp"],
    "Document" : ["pdf", "docx", "doc", "txt", "xlsx"],
    "Audio" : ["mp3", "wav", "aac"],
    "Video" : ["mp4", "mov", "avi", "mkv"],
    "code" : ["py", "js", "html", "css", "java", "cpp"],
    "Archive" : ["zip", "rar", "tar", "gz"]
}

#Dictionary to keep count of files moved
counts = {
    "Images": 0,
    "Document": 0,
    "Audio": 0,
    "Video": 0,
    "code": 0,
    "Archive": 0,
    "No Extension": 0,
    "Others": 0
}


for file in files:
    #Get file name and Extension
    name, extensions = os.path.splitext(file)
    #Remove the dot in the extension and convert to lower case
    ext = extensions[1:].lower()
    default_folder = "Others"

    new_name = file


    #Check if folder
    folder_check = os.path.join(which_folder, file)
    if not os.path.isfile(folder_check):
        continue

    #Check for no extension
    if ext == "":
        default_folder = "No Extension"

    for folder, extensions in file_type.items():
        if ext in extensions:
            default_folder = folder
            break

    print(file, default_folder)

    #Build Folder path
    folder_path = os.path.join(which_folder, default_folder)

    #Create folder if it does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    #Source file path
    source = os.path.join(which_folder, file)

    #Destination file path, add name if file exists
    destination = os.path.join(folder_path, new_name)
    i = 1
    while os.path.exists(destination):
        new_name = f"{name} ({i}){extensions}"
        destination = os.path.join(folder_path, new_name)
        i+=1

    #Move file to the destination folder
    counts[default_folder] += 1
    shutil.move(source, destination)

    print(f"Moved: {file} to {default_folder} folder")

#Print summary of moved files
print("\nSummary of moved files:")
for folder, count in counts.items():
    print(f"{folder}: {count} files")