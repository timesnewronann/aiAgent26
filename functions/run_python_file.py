import os


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
        if os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # check if the file path doesn't end with .py
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # use a subprocess to run the file use this command to run
        command = ["python", absolute_path]

        # if there are any extra args add them to the commands list
        command.extend(args)

    except Exception as e:
        return f"Error: {e}"
