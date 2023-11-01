# ChatGPT Big File Reader

This application allows you to read large files and send their content to ChatGPT using the `chatgptmax` package. 

## Features
- Reads large files effectively.
- Sends the content of these files to ChatGPT.
- Returns responses from ChatGPT.

## Prerequisites
Before you can use this application, you need to:
1. Make sure that you have the necessary packages installed. These can be found in the `requirements.txt` file.
2. Set the environment variable `OPENAI_API_KEY` with your OpenAI API key. Ensure you have access to the API.
    - For more details on the OpenAI API and how to get your key, refer to: [OpenAI API Reference](https://form.openai.com/docs/api-reference).

## Installation

1. Clone this repository to your local machine.
```
git clone https://github.com/matheuspolitano/BigFileReader
```

2. Navigate to the directory and install the necessary packages.
```
cd <directory_name>
pip install -r requirements.txt
```

## Set your Key

Please set the OPENAI_API_KEY environment variable with your OpenAI API key. For more details, refer to: https://form.openai.com/docs/api-reference

## Usage

1. Edit the `main.py` script to specify the path to your desired file in the `file_path` variable.
2. Define your prompt in the `prompt_text` variable.
3. Run the script:
```
python main.py
```
This will read the content of the specified file, send it to ChatGPT, and print the responses.

## Code Overview

The main functionality is present in the `main.py` script:

- Import necessary modules.
- Define a function, `read_file_content()`, to read the content of the file.
- Use this function to read the content and send it to ChatGPT.
- Print the received responses from ChatGPT.

## Contributing

Feel free to submit pull requests or issues if you have any improvements or feedback.

## Owner
This project is owned and maintained by Matheus Politano. You can connect with him or check out his other projects:
- [GitHub](https://github.com/matheuspolitano?tab=repositories)
- [LinkedIn](https://www.linkedin.com/in/matheus-politano-08b762123/)

## License

[MIT](LICENSE)