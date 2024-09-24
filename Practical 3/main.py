import os
import fnmatch

def list_files_by_prefix(directory, prefix):
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            print(f"Either the directory '{directory}' does not exist or is not valid.")
            return

        # Filter files that start with the given prefix
        matching_files = fnmatch.filter(os.listdir(directory), f"{prefix}*")
        
        # Check if any files match the filter
        if not matching_files:
            print(f"No files starting with '{prefix}' were found in '{directory}'.")
        else:
            print(f"Files starting with '{prefix}' in '{directory}':")
            for filename in matching_files:
                print(filename)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take user input for directory and file prefix
    directory = input("Enter Directory: ")
    prefix = input("Enter first letter (or prefix) of file: ")
    
    # List the matching files
    list_files_by_prefix(directory, prefix)
