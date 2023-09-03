import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")

# Create subfolders for different file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"]
}

for folder_name in file_types:
    folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files into respective subfolders
for file_name in os.listdir(desktop_path):
    if file_name.endswith(tuple(sum(file_types.values(), []))):  # Check if file extension matches any of the types
        for folder_name, extensions in file_types.items():
            if os.path.splitext(file_name)[1] in extensions:
                source_path = os.path.join(desktop_path, file_name)
                destination_path = os.path.join(desktop_path, folder_name, file_name)
                shutil.move(source_path, destination_path)
                break

print("Files organized successfully!")
