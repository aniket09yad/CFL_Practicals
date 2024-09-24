import os

def search_word_in_file(search_word):
    file_path = 'sample.txt'  # Path to 'sample.txt' in the current directory

    try:
        # Check if the file exists in the current directory
        if not os.path.exists(file_path):
            print(f"File '{file_path}' not found in the current directory.")
            return
        
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the first line of the file
            line = file.readline()
            
            # Split the line into words
            words = line.split()
            
            # Search for the word (ignoring case)
            if search_word.lower() in [word.lower() for word in words]:
                print(f"Text '{search_word}' Found")
            else:
                print(f"Text '{search_word}' Not Found")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the word to search from the user
    search_word = input("Enter the word you want to search: ")
    
    # Search for the word in 'sample.txt' file
    search_word_in_file(search_word)
