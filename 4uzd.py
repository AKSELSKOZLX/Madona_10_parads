def open_file(file_name, file_ext):
    try:
        file_path = file_name + "." + file_ext
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File with name '{file_name}' and extension '{file_ext}' not found.")
    except PermissionError:
        print(f"You do not have permission to read the file '{file_name}.{file_ext}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    file_ext = input("Enter the file extension: ")
    open_file(file_name, file_ext)