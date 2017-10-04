import os
import argparse


def find_duplicates(root_dir_path):
    files_in_folder = []
    duplicates = []
    for root, dir, files in os.walk(root_dir_path):
        for file in files:
            file_path = "/".join([root, file])
            if os.path.islink(file_path):
                continue
            if (file, os.stat(file_path).st_size) in files_in_folder:
                duplicates.append(file_path)
            else:
                files_in_folder.append((file, os.stat(file_path).st_size))
    return duplicates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path", help="write name of json file")
    duplicates = find_duplicates(parser.parse_args().dir_path)
    if duplicates:
        print("This files have duplicates: ")
        for duplicate in duplicates:
            print(duplicate)
    else:
        print("There are no duplicates in this folder")
