import time
from pinecone import Pinecone, ServerlessSpec, Index
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

def init_pinecone() -> Pinecone:
    return _connect_pinecone()

def _connect_pinecone() -> Pinecone:
    try:
        return Pinecone(api_key=PINECONE_API_KEY)
    except Exception as e:
        print(f'Error: faieled to connect pinecone. {e}')
        