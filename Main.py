from pathlib import Path
from shutil import move

if __name__ == "__main__":
    root_path = Path.home() / "Downloads" #use ... / "Desktop" to clear your desktop

    sort_files_extensions = {".jar": "my_jar_files", ".py": "python_files", ".exe": "executable_files"} #please customise these to your own preferences
    other_files = "other_files" #all other files will be stored here

    for item in list(sort_files_extensions.keys()):
        if not (root_path / sort_files_extensions[item]).exists():
            (root_path / sort_files_extensions[item]).mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {sort_files_extensions[item]}")

        if not(root_path / other_files).exists():
            (root_path / other_files).mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {other_files}")

    files_moved_total = 0

    for item in root_path.glob("*.*"): #find all files in the root directory
        for item_2 in list(sort_files_extensions.keys()): #get all file extensions
            if str(item).endswith(item_2): #check if file endswith specific file extension
                move(str(root_path / item), str(root_path / sort_files_extensions[item_2])) #move item to the corresponding folder
                print(f"Moved item: {item}")
                files_moved_total += 1 #count all files moved

    for item in root_path.glob("*.*"): #find all files left in the root directory
        if not item.is_dir(): #check if file is not a directory (folder)
            move(str(root_path / item), str(root_path / other_files)) #move file to other_files folder
            print(f"Moved item: {item}")
            files_moved_total += 1 #count all files moved

    print(f"\nCleared your folder! {files_moved_total} files were moved!")