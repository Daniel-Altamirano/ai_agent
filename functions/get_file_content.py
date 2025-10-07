import os
from .config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    working_dir = os.path.realpath(os.path.expanduser(working_directory))
    target_file_path = os.path.join(working_dir, file_path)

    if not os.path.commonpath([working_dir, target_file_path]) == working_dir:
        return f'Error: Cannot read "{target_file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{target_file_path}"'

    with open(target_file_path, 'r') as f:
        try:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f"""[...File "{target_file_path}" truncated at {MAX_CHARS} characters]"""
            return file_content_string
        except Exception as e:
            return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path, relative to the working directory, to the file to read.",
            )
        }
    )
)