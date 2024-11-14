import openai
from dataclasses import dataclass

@dataclass
class ChatGPTConfig:
    prompt: str
    model: str
    temperature: float
    system_content: str

def parse_text_with_chatgpt(config: ChatGPTConfig):
    prompt = config.prompt
    model = config.model
    temperature = config.temperature
    system_content = config.system_content
    
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in parse_text_with_chatgpt: {e}")
        return None