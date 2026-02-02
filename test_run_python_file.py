from functions.run_python_file import run_python_file


def main():
    # print the results in a readable way
    calculator_instructions = run_python_file("calculator", "main.py")

    print("Result for calculator instructions:")
    print(calculator_instructions)

    calculator_result_args = run_python_file("calculator", "main.py", ["3 + 5"])

    print("Result for 'calculator' file:")
    print(calculator_result_args)

    calculator_tests = run_python_file("calculator", "tests.py")
    print("Successful run for 'calculator' file:")
    print(calculator_tests)

    calculator_main = run_python_file("calculator", "../main.py")
    print("Return an error for 'calculator' file:")
    print(calculator_main)

    calculator_nonexistent = run_python_file("calculator", "nonexistent.py")

    print("Result for 'nonexistent.py' file:")
    print(calculator_nonexistent)

    calculator_lorem_text = run_python_file("calculator", "lorem.txt")
    print("Result for 'lorem.txt' file:")
    print(calculator_lorem_text)


#     Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True
if __name__ == "__main__":
    main()
