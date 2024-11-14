from pinecone import Pinecone

def create_query_vector(pc: Pinecone) -> any:
    try:
        query = "Tell me about the tech company known as Apple."

        embedding = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[query],
            parameters={
                "input_type": "query"
            }
        )
        
        return embedding
    except Exception as e:
        print(f'Error: failed to create query vector. {e}')