import time
from pinecone import Pinecone, ServerlessSpec, Index
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

index_name = "quickstart"

data = [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
]

def process_pinecone():
    pc = init_pinecone()
    # delete_index(pc)
    index = upsert_data(pc)
    embedding = create_query_vector(pc)
    run_similarity_search(index, embedding)

def init_pinecone() -> Pinecone:
    return Pinecone(api_key=PINECONE_API_KEY)

def upsert_data(pc: Pinecone) -> Index:
    _create_index(pc)
    embeddings = _embed_data(pc)
    index = _execute_upsert_data(pc, embeddings)
    return index
        
def _create_index(pc: Pinecone):
    pc.create_index(
        name=index_name,
        dimension=1024, # Replace with your model dimensions
        metric="cosine", # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
    )
    
def _embed_data(pc: Pinecone) -> any:
    embeddings = pc.inference.embed(
        model="multilingual-e5-large",
        inputs=[d['text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )
    print(embeddings[0])
    return embeddings
    
def _execute_upsert_data(pc: Pinecone, embeddings: any) -> Index:
    # Wait for the index to be ready
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

    index = pc.Index(index_name)

    vectors = []
    for d, e in zip(data, embeddings):
        vectors.append({
            "id": d['id'],
            "values": e['values'],
            "metadata": {'text': d['text']}
        })

    index.upsert(
        vectors=vectors,
        namespace="ns1"
    )
    
    print(index.describe_index_stats())
    
    return index

def create_query_vector(pc: Pinecone) -> any:
    query = "Tell me about the tech company known as Apple."

    embedding = pc.inference.embed(
        model="multilingual-e5-large",
        inputs=[query],
        parameters={
            "input_type": "query"
        }
    )
    
    return embedding
    
def run_similarity_search(index: Index, embedding: any):
    results = index.query(
        namespace="ns1",
        vector=embedding[0].values,
        top_k=3,
        include_values=False,
        include_metadata=True
    )

    print(f"results: {results}")
    
def delete_index(pc: Pinecone):
    pc.delete_index(index_name)
    print(f"Index '{index_name}' has been deleted.")  
        