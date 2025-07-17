import os
import shutil
import sys

# Define file type categories
FILE_TYPES = {
    'PDF': ['.pdf'],
    'IMAGES': ['.jpg', '.jpeg', '.png', '.gif'],
    'DOCUMENTS': ['.docx', '.doc', '.txt'],
    'PYTHON': ['.py'],
    'EXCEL': ['.xlsx', '.xls'],
    'VIDEOS': ['.mp4', '.mov', '.avi'],
    'ARCHIVES': ['.zip', '.rar', '.7z'],
    'OTHERS': []
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Invalid path. Please enter a valid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, 'OTHERS')
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))

    print("✅ Files organized successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organize.py <folder_path>")
    else:
        folder = sys.argv[1]
        organize_files(folder)
