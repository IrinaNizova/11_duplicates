import os
import argparse


def find_duplicates(root_dir_path):
    files_in_folder = []
    duplicates = []
    for root, dir, file_names in os.walk(root_dir_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            if os.path.islink(file_path):
                continue
            file_size = os.path.getsize(file_path)
            if (file_name, file_size) in files_in_folder:
                duplicates.append((file_path, file_name))
            else:
                file_size = os.path.getsize(file_path)
                files_in_folder.append((file_name, file_size))
    duplicates.sort(key=lambda x: x[1])
    return duplicates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path", help="write name of json file")
    duplicates = find_duplicates(parser.parse_args().dir_path)
    if duplicates:
        print("This files have duplicates: ")
        for duplicate_name, _ in duplicates:
            print(duplicate_name)
    else:
        print("There are no duplicates in this folder")
