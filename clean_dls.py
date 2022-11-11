"""Clean Downloads folder

This script deletes all copies, installer files, setup files, .zip files,
.7z files, .stl files, .msi files from a specified file path.
This was created to delete all the junk and clutter from your downloads
folder that has been piling up.
"""

import os
from pathlib import Path

def file_deletion():
    """Gets and deletes the files from the user given files path

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    user_path = input("Enter your file path for deletion: ")
    if os.path.exists(user_path):
        os.chdir(os.path.join(user_path))
        all_files = os.listdir()
        files_to_del = []
        files_to_keep = []
        suffixes_to_del = [".zip", ".7z", ".stl", ".msi"]
        deletion = False

        for file in all_files:
            if (("setup" in str(file).lower()) or 
                ("installer" in str(file.lower())) or 
                ("(" and ")" in file or 
                Path(file).suffix in suffixes_to_del)):

                files_to_del.append(file)
            else:
                files_to_keep.append(file)

        deletion_string = "No Files to delete." if len(files_to_del) == 0 else "Deleting Files: "
        print(deletion_string)
        if deletion_string != "No Files to delete.":
            for file in files_to_del:
                print(file)
            # print("-----------------")
            # print("Files to keep: ")
            # for file in files_to_keep:
            #     print(file)
            
            user_choice = input("Are you ready to delete? Y/N: ")
            deletion = True if user_choice.upper() == "Y" else False
            if deletion:
                for file in files_to_del:
                    if os.path.exists(file):
                        os.remove(file)
                    else:
                        print("{} does not exist.".format(file))
        else:
            print("Path does not exist.")
    print("Thank you for using clean_dls.py")

if __name__ == "__main__":
    file_deletion()