import time
import threading
import os

def copy_file(file_name, source_dir, dest_dir):
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    print(source_path, "-->", dest_path)

    # Copy file
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break

if __name__ == "__main__":
    source_dir = "bunny"
    dest_dir = "bunny-copy"

    try:
        os.mkdir(dest_dir)
    except:
        print("bunny-copy already existed. No file is generated.")

    file_list = os.listdir(source_dir)
    for file_name in file_list:
        #copy_file(file_name, source_dir, dest_dir)
        sub_thread = threading.Thread(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_thread.start()
