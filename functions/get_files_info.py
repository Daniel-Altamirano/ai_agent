import os

def get_files_info(working_directory, directory="."):
    working_dir = os.path.realpath(os.path.expanduser(working_directory))
    target_dir = os.path.realpath(os.path.join(working_dir, directory))

    if not os.path.commonpath([working_dir, target_dir]) == working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        contents = os.listdir(target_dir)
        contents_info = []

        for item in contents:
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            contents_info.append(f"- {item}: {file_size=} bytes, {is_dir=}")

        contents_info = "\n".join(contents_info)
        return contents_info
    except Exception as e:
        return f"Error listing files: {e}"
    