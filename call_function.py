from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python
from functions.get_file_content import schema_file_content

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_run_python,
        schema_write_file,
        schema_file_content
    ]
)
