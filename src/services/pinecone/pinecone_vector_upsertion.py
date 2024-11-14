import time
from pinecone import Pinecone, ServerlessSpec, Index

index_name = "quickstart"
sample_data = [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
]

def upsert_data(pc: Pinecone) -> Index:
    _create_index(pc)
    embeddings = _embed_data(pc)
    _wait_for_index(pc)
    index = _upsert_vectors_to_index(pc, embeddings)
    return index
        
def _create_index(pc: Pinecone):
    try:
        pc.create_index(
            name=index_name,
            dimension=1024, # Replace with your model dimensions
            metric="cosine", # Replace with your model metric
            spec=ServerlessSpec( 
                cloud="aws",
                region="us-east-1"
            ) 
        )
    except Exception as e:
        print(f'Error: failed to create index. {e}')
    
def _embed_data(pc: Pinecone) -> any:
    try:
        embeddings = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[d['text'] for d in sample_data],
            parameters={"input_type": "passage", "truncate": "END"}
        )
        print(embeddings[0])
        return embeddings
    except Exception as e:
        print(f'Error: failed to embed data. {e}')
        
def _wait_for_index(pc: Pinecone):
    try:
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)
    except Exception as e:
        print(f'Error: failed to waiting index. {e}')
    
def _upsert_vectors_to_index(pc: Pinecone, embeddings: any) -> Index:
    try:
        index = _fetch_index(pc, index_name)

        vectors: list = _initialize_vectors()
        vectors: list = _convert_embeddings_to_vectors(embeddings, vectors)
        
        index = _upsert_index(index, vectors)
        _confirm_index_stats(index)
        
        return index
    except Exception as e:
        print(f'Error: failed to upsert data. {e}')

def _fetch_index(pc: Pinecone, index_name: str) -> Index:
    return pc.Index(index_name)

def _initialize_vectors() -> list:
    return []

def _convert_embeddings_to_vectors(embeddings: any, vectors: list) -> list:
    for d, e in zip(sample_data, embeddings):
        vectors.append({
            "id": d['id'],
            "values": e['values'],
            "metadata": {'text': d['text']}
        })
    return vectors

def _upsert_index(index: Index, vectors: list) -> Index:
    index.upsert(
        vectors=vectors,
        namespace="ns1"
    )
    return index

def _confirm_index_stats(index: Index):
    print(index.describe_index_stats())