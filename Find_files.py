import os

root_dir_path = "/home/vipikuma/Documents"
new_file_path = os.path.join(root_dir_path, "../all_files")

def copyfile(src, dest):
    with open(src, "rb") as source_file:
        with open(dest, "wb") as destination_file:
            destination_file.write(source_file.read())


def CopyAllFiles(root_dir_path, new_file_path, skip_hidden=True):
    os.makedirs(new_file_path, exist_ok=True)
    for root, dirs, files in os.walk(root_dir_path):
        if not root.split("/")[-1].startswith("."):
            for file in files:
                old_file, new_file = os.path.join(root_dir_path, root, file), os.path.join(new_file_path, file)
                print("Copying file: %s into %s" % (old_file, new_file_path))
                copyfile(old_file, new_file)
    return True

if CopyAllFiles(root_dir_path, new_file_path):
    print("Done with copying all the Files")
