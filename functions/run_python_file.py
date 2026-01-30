import os


def run_python_file(working_directory, file_path, args=None):
    # 1. Validate that the path to directory is inside the working directory
    absolute_path = os.path.abspath(working_directory)
    print(f"Absolute Path: {absolute_path}")

    # 2. Build the target path
    target_path = os.path.normpath(os.path.join(absolute_path, file_path))

    # 3. Validate that the path
    valid_target_path = os.path.commonpath([absolute_path, target_path]) == absolute_path
