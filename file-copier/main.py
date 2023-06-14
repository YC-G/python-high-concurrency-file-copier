import time
import multiprocessing
import os
import shutil


def copy_file(file_name, source_dir, dest_dir):
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    print(source_path, "-->", dest_path)

    shutil.copyfile(source_path, dest_path)

if __name__ == '__main__':
    # Get current directory
    #current_dir = os.getcwd()
    #print(current_dir)

    # Get source directory and target directory
    source_dir = "bunny"
    # dest_dir = "/Users/yuchenguo/Desktop/bunny-copy"
    dest_dir = "bunny-copy"

    try:
        os.mkdir(dest_dir)
    except:
        print("bunny-copy already existed. No file is generated.")

    # Get the name of files to be copied
    file_list = os.listdir(source_dir)
    print(file_list)

    # Copy files
    for file in file_list:
        #copy_file(file, source_dir, dest_dir)
        sub_process = multiprocessing.Process(target=copy_file, args=(file, source_dir, dest_dir))
        sub_process.start()