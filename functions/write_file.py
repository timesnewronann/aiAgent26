import os


def write_file(working_directory, file_path, content):
    try:
        # 1. Validate that the path to directory is inside the working directory -> ex /Users/timesnewronan/workspace/github.com/timesnewronann/aiAgent26/aiAgent26/calculator
        absolute_path = os.path.abspath(working_directory)
        print(f"Absolute Path: {absolute_path}")

        # 2. Build the target path -> ex /Users/timesnewronan/workspace/github.com/timesnewronann/aiAgent26/aiAgent26/calculator/lorem.txt
        target_path = os.path.normpath(os.path.join(absolute_path, file_path))
        print(f"Target Path {target_path}")

        # Checking that the longest common path is exactly the file path  -> target_dir is inside the file path
        valid_target_path = os.path.commonpath([absolute_path, target_path]) == absolute_path
        print(f"Is this valid target path? {valid_target_path}")

        # Check if target dir is in working_dir_abs
        if valid_target_path != True:
            # if the file path is outside of the working directory return an error
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # if the file path points to an existing directory
        if os.path.isdir(valid_target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # check if the necessary parent directories of the file path exists
        # Use os.mkdirs()

    except Exception as e:
        return f"Error: {e}"
