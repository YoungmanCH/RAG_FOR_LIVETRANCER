def read_text_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()
    
def format_prompt(prompt: list, text: str) -> str:
    return prompt.format(read_text=text)