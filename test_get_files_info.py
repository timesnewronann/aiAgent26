from functions.get_files_info import get_files_info


def main():
    # print the results in a readable way
    calculator_result = get_files_info("calculator", ".")

    print("Result for current directory:")
    print(calculator_result)

    calculator_result_pkg = get_files_info("calculator", "pkg")

    print("Result for 'pkg' directory:")
    print(calculator_result_pkg)

    calculator_result_bin = get_files_info("calculator", "/bin")

    print("Result for '/bin' directory:")
    print(calculator_result_bin)

    calculator_result_slash = get_files_info("calculator", "../")

    print("Result for '../' directory:")
    print(calculator_result_slash)


#     Result for current directory:
#   - main.py: file_size=719 bytes, is_dir=False
#   - tests.py: file_size=1331 bytes, is_dir=False
#   - pkg: file_size=44 bytes, is_dir=True
if __name__ == "__main__":
    main()
