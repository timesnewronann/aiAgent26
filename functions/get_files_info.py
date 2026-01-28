import os


def get_files_info(working_directory, directory="."):

    # 1. Validate that the path to directory is inside the working directory
    absolute_path = os.path.abspath(working_directory)

    # 2. Build the target directory
    target_dir = os.path.normpath(os.path.join(absolute_path, directory))

    # Checking that the longest common path is exactly the working dir -> target_dir is inside the working dir
    valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

    # Check if target dir is in working_dir_abs
    if valid_target_dir != True:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    contents = []
    # iterate over the items in the target_dir
    for item_name in os.listdir(target_dir):
        # store the name, file size, and whether it is a directory
        full_path = os.path.join(target_dir, item_name)

        file_size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)

        line = f"- {item_name}: file_size={file_size} bytes, is_dir={is_dir}"
        contents.append(line)

    return "\n".join(contents)
