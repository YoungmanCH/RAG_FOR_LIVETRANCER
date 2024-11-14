import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from ..services.pinecone.pinecone_handler import process_pinecone
from ..services.chatgpt_services.readme_converter import process_readme_file_with_chatgpt
from ..utils.save_to_json_file import save_to_json_file

def test():
#    _test_process_pinecone()
   _test_parse_readme()
   _test_parse_readme_ja()
#    _test_parse_readme_tree()
   
def _test_process_pinecone():
    process_pinecone()
    
def _test_parse_readme():
    readme_parsed_json = process_readme_file_with_chatgpt("fetched_data/fetched_README.md")
    save_to_json_file(readme_parsed_json, "readme.json")
    
def _test_parse_readme_ja():
    readme_ja_parsed_json = process_readme_file_with_chatgpt("fetched_data/fetched_README_ja.md")
    save_to_json_file(readme_ja_parsed_json, "readme_ja.json")
    
def _test_parse_readme_tree():
    readme_tree_parsed_json = process_readme_file_with_chatgpt("fetched_data/fetched_README_tree.md")
    save_to_json_file(readme_tree_parsed_json, "readme_tree.json")
    
def main():
    test()

if __name__ == "__main__":
    main()
