# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file in write mode
        with open("my_file.txt", 'w') as file:
            # Write at least three lines of text
            file.write("This is the first line of text.\n")
            file.write("Here is a number: 42\n")
            file.write("And this is the third line.\n")
        print("File created and written to successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error creating file: {e}")
    finally:
        print("Finished attempting to create and write to the file.")

def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError as e:
        print(f"Error reading file: {e}")
    finally:
        print("Finished attempting to read the file.")

def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text
            file.write("Appending a new line: Hello World!\n")
            file.write("Another number: 123\n")
            file.write("Yet another line to add.\n")
        print("Successfully appended to the file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Finished attempting to append to the file.")

if __name__ == "__main__":
    create_file()  # Create and write to the file
    read_file()    # Read and display the file contents
    append_to_file()  # Append new content to the file
    read_file()    # Read and display the file contents again
