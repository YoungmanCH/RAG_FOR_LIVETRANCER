import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from .pinecone.pinecone import process_pinecone

def test():
   process_pinecone()
  
def main():
    test()

if __name__ == "__main__":
    main()
