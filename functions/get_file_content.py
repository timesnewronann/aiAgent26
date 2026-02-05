import os
from config import MAX_CHARS
from google import genai
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file content, checks if the file exceeds the limit, then returns the file content with truncation note if needed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path of the file to read, from the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    try:
        # 1. Validate that the path to directory is inside the working directory -> ex /Users/timesnewronan/workspace/github.com/timesnewronann/aiAgent26/aiAgent26/calculator
        absolute_path = os.path.abspath(working_directory)

        # 2. Build the target path -> ex /Users/timesnewronan/workspace/github.com/timesnewronann/aiAgent26/aiAgent26/calculator/lorem.txt
        target_path = os.path.normpath(os.path.join(absolute_path, file_path))

        # Checking that the longest common path is exactly the file path  -> target_dir is inside the file path
        valid_target_path = os.path.commonpath([absolute_path, target_path]) == absolute_path

        # Check if target dir is in working_dir_abs
        if valid_target_path != True:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # guard rail to check if it is a file
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # read the file
        try:
            # open the file in read mode
            # read only 1000 characters max
            with open(target_path, 'r', encoding="utf-8") as f:
                file_contents = f.read(MAX_CHARS)

                # check if the file was larger than the limit

                if f.read(1):
                    file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_contents

        except Exception as e:
            return f"Error: {e}"

    except Exception as e:
        return f"Error: {e}"
