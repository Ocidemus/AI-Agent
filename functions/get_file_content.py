# import os

# def get_file_content(working_directory, file_path):
#     abs_working_dis = os.path.abspath(working_directory)
#     target_dir = os.path.abspath(os.path.join(working_directory, file_path)) if file_path else abs_working_dis

#     if not target_dir.startswith(abs_working_dis):
#         return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
#     if not os.path.isfile(target_dir):
#         return f'Error: File not found or is not a regular file: "{file_path}"'
    
#     try:
#         MAX_CHARS = 10000

#         with open(file_path, "r") as f:
#             content = f.read()
#             if len(content) > MAX_CHARS:
                
#                 new_content = content[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'
#                 f.seek(0)
#                 f.write(new_content)
#                 f.truncate()
#                 return new_content
#             else:
#                 return content
    
           
    
#     except Exception as e:
#         return f"Error: {str(e)}"
         
         
import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
