from ...utils.util import read_text_file, format_prompt
from .prompts import README_PROMPT
import os
from dotenv import load_dotenv
import openai
from openai import ChatCompletion
from .text_parser import ChatGPTConfig, parse_text_with_chatgpt

load_dotenv()
OPENAI_API_KEY = os.getenv("ENV_OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def process_readme_file_with_chatgpt(file_path):
    read_text = read_text_file(file_path)
    parsed_sections = _chatgpt_parse_text(read_text)
    if parsed_sections:
        print(f"Parsed Sections (JSON): {parsed_sections}")
        return parsed_sections
    else:
        print("Failed to parse text.")
        return None

def _chatgpt_parse_text(read_text: str):
    try:
        prompt = format_prompt(README_PROMPT, read_text)
        config = ChatGPTConfig(prompt=prompt, model="gpt-4", temperature=1.0, system_content="あなたはREADME.mdファイルをjson形式で解析する専門家です。")
        response = parse_text_with_chatgpt(config)
        return response
    except Exception as e:
        print(f"Error parsing text with ChatGPT: {e}")
        return None
