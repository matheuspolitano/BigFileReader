# First, import the necessary modules and the function
import os

from chatgptmax import send

# Define a function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Use the function
if __name__ == "__main__":
    # Specify the path to your file
    file_path = "script.txt"
    
    # Read the content of the file
    file_content = read_file_content(file_path)
    
    # Define your prompt
    prompt_text = "Translate to french my typescript:"
    
    # Send the file content to ChatGPT
    responses = send(prompt=prompt_text, text_data=file_content)
    
    # Print the responses
    for response in responses:
        print(response)