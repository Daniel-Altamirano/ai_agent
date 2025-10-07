import os

def write_file(working_directory, file_path, content):
    working_dir = os.path.realpath(os.path.expanduser(working_directory))
    target_file_path = os.path.join(working_dir, file_path)
    target_dir = os.path.dirname(target_file_path)

    if not os.path.commonpath([working_dir, target_file_path]) == working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_dir):
        try:
            os.makedirs(os.path.dirname(target_dir))
        except Exception as e:
            return f"Error: {e}"
    
    try:
        with open(target_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
