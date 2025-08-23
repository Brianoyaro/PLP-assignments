def read_write(file_name: str):
    try:
        # Try to open and read file
        with open(file_name, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print("File doesn't exist.")
        return
    except PermissionError:
        print("You don’t have permission to read this file.")
        return

    # Write a modified version to a new file
    with open("modified.txt", 'w') as file:
        information = data.upper()
        file.write(information)

    print("File has been modified and saved as 'modified.txt'.")

# Ask user for filename
file_name = input("What file do you want to open: ")
read_write(file_name)

