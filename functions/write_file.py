import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_work_path = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory,file_path))
    
    if not target_dir.startswith(abs_work_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.exists(file_path):
        try:
            os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        
        with open(target_dir,"w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
        
    except Exception as e:
        return f"Error: {str(e)}"
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file in the specified path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base directory where file writes are allowed. All paths must stay within this."
            ),
            "path_file": types.Schema(
                type=types.Type.STRING,
                description="The path to the file (relative to the working directory) where the content should be written."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the specified file."
            )
        },
        required=["working_directory", "path_file", "content"]
    )
)
