import os 
import shutil
from logger import FolderLogger

def organise_folder(folder_path, logger):
    files = os.listdir(folder_path)
    
    for file in files:
        #Get file name and Extension
        name, ext = os.path.splitext(file)
        #Remove the dot in the extension and convert to lower case
        extension = ext[1:].lower()
        default_folder = "Others"
        new_name = file

        #Check if its a folder
        folder_check = os.path.join(folder_path, file)
        if not os.path.isfile(folder_check):
            continue

        #Check for no extension
        if extension == "":
            default_folder = "No Extension"

        #Determine the correct folder based on extension
        for folder, extensions in logger.file_types.items():
            if extension in extensions:
                default_folder = folder
                break
        
        print(file, default_folder)

        #Build Folder path
        file_to_organise = os.path.join(folder_path, default_folder)

        #Create folder if it does not exist
        if not os.path.exists(file_to_organise):
            os.makedirs(file_to_organise)
        
        #Source file path
        source =  os.path.join(folder_path, file)

        #Destination file path, add name if file exists
        destination = os.path.join(file_to_organise, new_name)
        i = 1
        while os.path.exists(destination):
            new_name = f"{name} ({i}){ext}"
            destination = os.path.join(file_to_organise, new_name)
            i += 1
        
        #Move file to the destination folder
        shutil.move(source, destination)
        logger.log_file_move(file, default_folder)

        #print(f"Moved: {file} to {default_folder} folder")