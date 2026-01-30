from functions.get_file_content import get_file_content


def main():
    # print the results in a readable way
    calculator_lorem = get_file_content("calculator", "lorem.txt")

    print("Result for current file:")
    print(calculator_lorem)

    calculator_result_main = get_file_content("calculator", "main.py")

    print("Result for 'main.py' file:")
    print(calculator_result_main)

    calculator_result_pkg_calculator = get_file_content("calculator", "pkg/calculator.py")

    print("Result for 'pkg/calculator.py' file:")
    print(calculator_result_pkg_calculator)

    calculator_result_error = get_file_content("calculator", "/bin/cat")

    print("Result for '../' directory:")
    print(calculator_result_error)

    calculator_result_error_two = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'pkg/does_not_exist.py' directory:")
    print(calculator_result_error_two)


#     Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True
if __name__ == "__main__":
    main()
