import os

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
        
    