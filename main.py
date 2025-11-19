import os
from sorter import organise_folder
from logger import FolderLogger

def main():

    while True:
        print("\n===== FOLDER ORGANISER =====")
        print("[1] Organise a folder")
        print("[2] Exit")
        choice = input("Enter your choice: ").strip()
    
        if choice == "1":
            folder_path = input("Enter the folder path to organise: ").strip()

            if not os.path.exists(folder_path):
                print("Error: The folder does not exist.")
                continue
            if not os.path.isdir(folder_path):
                print("Error: The path is not a directory.")
                continue
                    
            #Initialise, call, and log
            logger = FolderLogger()
            organise_folder(folder_path, logger)
            logger.summaryLog()
            
            #Sorting Algorithm
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1 or 2.")
            
if __name__ == "__main__":
    main()