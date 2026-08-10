import os
import shutil

folder_path = r"C:\Users\rdeep\OneDrive\Desktop\AI\Python\File Organizer\Test Folder"

folders = ["Images", "Musics", "Videos", "Documents"]
for folder in folders:
    path = os.path.join(folder_path, folder)

    if not os.path.exists(path):
        os.mkdir(path)


files = os.listdir(folder_path)
for file in files:
    source = os.path.join(folder_path, file)

    if os.path.isdir(source):
        continue

    if file.endswith((".jpg", ".jpeg", ".png")):
        destination = os.path.join(folder_path, "Images", file)
        shutil.move(source, destination)
    elif file.endswith((".mp3")):
        destination = os.path.join(folder_path, "Musics", file)
        shutil.move(source, destination)
    elif file.endswith((".mp4")):
        destination = os.path.join(folder_path, "Videos", file)
        shutil.move(source, destination)
    elif file.endswith((".pdf", ".txt")):
        destination = os.path.join(folder_path, "Documents", file)
        shutil.move(source, destination)



