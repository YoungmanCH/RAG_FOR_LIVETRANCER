from pinecone import Index

def run_similarity_search(index: Index, embedding: any):
    try:
        results = index.query(
            namespace="ns1",
            vector=embedding[0].values,
            top_k=3,
            include_values=False,
            include_metadata=True
        )

        print(f"results: {results}")
    
        return embedding
    except Exception as e:
        print(f'Error: failed to run similarity search. {e}')