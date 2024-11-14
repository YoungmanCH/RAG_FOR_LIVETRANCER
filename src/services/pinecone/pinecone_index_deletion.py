from pinecone import Pinecone

index_name = "quickstart"
    
def delete_index(pc: Pinecone):
    try:
        pc.delete_index(index_name)
        print(f"Index '{index_name}' has been deleted.")  
    except Exception as e:
        print(f'Error: failed to delete index data. {e}')
        