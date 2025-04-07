def read_and_modify_file(input_filename, output_filename):
    try:
        # Attempt to open the input file in read mode
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.read()

        # Modify the content (example: convert the content to uppercase)
        modified_content = content.upper()

        # Attempt to open the output file in write mode
        with open(output_filename, 'w') as outfile:
            # Write the modified content to the new file
            outfile.write(modified_content)
        
        print(f"The modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write the file {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input and output filenames
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to write to: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
