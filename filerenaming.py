import os
from datetime import datetime

def rename_files_in_directory(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            print(file)
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            new_name = f"{timestamp}_{file}"
            old_path = os.path.join(directory_path, file)
            new_path = os.path.join(directory_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {file} to {new_name}")
        else:
            print(f"Skipped: {file} (not an image file ")


if __name__ == '__main__':
    directory = r'.\img'
    rename_files_in_directory(directory)
