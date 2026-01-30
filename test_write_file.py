from functions.write_file import write_file


def main():
    # print the results in a readable way
    calculator_lorem = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")

    print("Result for current file:")
    print(calculator_lorem)

    # calculator_result_main = get_file_content("calculator", "main.py")

    # print("Result for 'main.py' file:")
    # print(calculator_result_main)

    calculator_result_pkg_calculator = write_file(
        "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")

    print("Result for 'pkg/morelorem.txt' file:")
    print(calculator_result_pkg_calculator)

    # calculator_result_error = get_file_content("calculator", "/bin/cat")

    # print("Result for '../' directory:")
    # print(calculator_result_error)

    calculator_result_error_two = write_file(
        "calculator", "/tmp/temp.txt", "this should not be allowed")

    print("Result for '/tmp/temp.txt' directory:")
    print(calculator_result_error_two)


#     Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True
if __name__ == "__main__":
    main()
