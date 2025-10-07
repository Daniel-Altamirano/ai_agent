import os

def get_files_info(working_directory, directory="."):
    working_directory = os.path.realpath(os.path.expanduser(working_directory))
    full_path = os.path.realpath(os.path.join(working_directory, directory))
    #print(f"{full_path=}")

    if not os.path.commonpath([working_directory, full_path]) == working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'


    contents = os.listdir(full_path)
    #print(f"{contents=}")
    contents_info = []

    for item in contents:
        item_path = os.path.join(full_path, item)
        #print(f"{item_path=}")
        file_size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        contents_info.append(f"- {item}: {file_size=} bytes, {is_dir=}")

    contents_info = "\n".join(contents_info)
    #print(f"{contents_info=}")
    return contents_info
    