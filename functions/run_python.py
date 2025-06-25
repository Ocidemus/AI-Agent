import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path,args=None):
    abs_work_path = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory,file_path))
    
    if not target_dir.startswith(abs_work_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_dir):
        return f'Error: File "{file_path}" not found.'
    
    if not target_dir.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", target_dir]
        if args:
            commands.extend(args)
        
        result = subprocess.run(
            commands,
            timeout = 30,
            capture_output = True,
            cwd = abs_work_path ,
            text=True,
            ) 
        
        output = result.stdout
        error_output = result.stderr
        messages = []
        
        if output:
            messages.append(f"STDOUT:\n{output}")
            
        if error_output:
            messages.append(f"STDERR:\n{error_output}")
        
        if result.returncode !=0:
            messages.append(f"Process exited with code {result.returncode}")

        return "\n".join(messages) if messages else "No output produced."
    
    except Exception as e :
        return f"Error: executing Python file: {e}"
            


schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
# import os
# import subprocess
# from google.genai import types


# def run_python_file(working_directory, file_path, args=None):
#     abs_working_dir = os.path.abspath(working_directory)
#     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
#     if not abs_file_path.startswith(abs_working_dir):
#         return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
#     if not os.path.exists(abs_file_path):
#         return f'Error: File "{file_path}" not found.'
#     if not file_path.endswith(".py"):
#         return f'Error: "{file_path}" is not a Python file.'
#     try:
#         commands = ["python", abs_file_path]
#         if args:
#             commands.extend(args)
#         result = subprocess.run(
#             commands,
#             capture_output=True,
#             text=True,
#             timeout=30,
#             cwd=abs_working_dir,
#         )
#         output = []
#         if result.stdout:
#             output.append(f"STDOUT:\n{result.stdout}")
#         if result.stderr:
#             output.append(f"STDERR:\n{result.stderr}")

#         if result.returncode != 0:
#             output.append(f"Process exited with code {result.returncode}")

#         return "\n".join(output) if output else "No output produced."
#     except Exception as e:
#         return f"Error: executing Python file: {e}"


# schema_run_python_file = types.FunctionDeclaration(
#     name="run_python_file",
#     description="Executes a Python file within the working directory and returns the output from the interpreter.",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "file_path": types.Schema(
#                 type=types.Type.STRING,
#                 description="Path to the Python file to execute, relative to the working directory.",
#             ),
#             "args": types.Schema(
#                 type=types.Type.ARRAY,
#                 items=types.Schema(
#                     type=types.Type.STRING,
#                     description="Optional arguments to pass to the Python file.",
#                 ),
#                 description="Optional arguments to pass to the Python file.",
#             ),
#         },
#         required=["file_path"],
#     ),
# )