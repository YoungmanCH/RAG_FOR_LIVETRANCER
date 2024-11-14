import os
import json

directory = "output"

def save_to_json_file(data: str, file_name: str):
    try:
        json_data = _convert_data_to_json(data)
        file_path = _combine_file_path(file_name)
        _write_json_file(json_data, file_path)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving JSON data: {e}")
        
def _convert_data_to_json(data: str) -> dict:
    return json.loads(data)
        
def _combine_file_path(file_name: str) -> str:
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, file_name)
    
def _write_json_file(json_data: dict, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
