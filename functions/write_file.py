import os
from google.genai import types


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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the content of a file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory, to the file to write to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file at the file path.",
            ),
        },
        required=["file_path", "content"],
    ),
)