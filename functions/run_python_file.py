import os
import subprocess
from google import genai
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file and checks if the file is not a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path of the file to read, from the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="A single command-line argument to pass to the Python file.",
                ),
                description="Optional list of command line arguments to pass to the Python file.",
            )
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        # 1. Validate that the path to directory is inside the working directory
        absolute_path = os.path.abspath(working_directory)
        print(f"Absolute Path: {absolute_path}")

        # 2. Build the target path
        target_path = os.path.normpath(os.path.join(absolute_path, file_path))

        # 3. Validate that the path
        valid_target_path = os.path.commonpath([absolute_path, target_path]) == absolute_path

        # Check if the target dir is in the working dir
        if valid_target_path != True:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # if the file path points to an existing directory checked the resolved path
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # check if the file path doesn't end with .py
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # use a subprocess to run the file use this command to run
        command = ["python", target_path]

        # if there are any extra args add them to the commands list, if args is empty this should cause an issue maybe check if args is not empty
        if args != None:
            command.extend(args)

        completedProcess = subprocess.run(command, cwd=absolute_path,
                                          capture_output=True, text=True, timeout=30)

        # use a list to handle the output
        output_parts = []

        if completedProcess.returncode != 0:
            output_parts.append(f"Process exited with code {completedProcess.returncode}")

        if not completedProcess.stdout and not completedProcess.stderr:
            output_parts.append("No output produced")

        if completedProcess.stdout:
            output_parts.append("STDOUT:\n" + completedProcess.stdout)

        if completedProcess.stderr:
            output_parts.append("STDERR:\n" + completedProcess.stderr)

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
