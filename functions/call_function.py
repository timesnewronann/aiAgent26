from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
import argparse

available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content,
                           schema_run_python_file, schema_write_file],
)

# function map
function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}


def call_function(function_call, verbose=False):
    # Handle the case if function_name is empty
    function_name = function_call.name or ""

    # If verbose
    if verbose == True:
        print(f"Calling function: {function_name}({function_call.args})")
    # not verbose
    else:
        print(f" - Calling function: {function_name}")

    # check if function name is not in function map -> return types.Content object that explains the error
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # Create and modify args:
    args = dict(function_call.args) if function_call.args else {}

    # Set "working_directory" to "./calculator" in the args dictionary
    args["working_directory"] = "./calculator"

    # Call the function
    function_result = function_map[function_name](**args)

    # wrap function result in a types.content using types.Part.from_function_response
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
