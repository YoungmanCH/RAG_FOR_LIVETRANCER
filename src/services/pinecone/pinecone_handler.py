from pinecone import Pinecone

from .pinecone_initialization import init_pinecone
from .pinecone_index_deletion import delete_index
from .pinecone_vector_upsertion import upsert_data
from .pinecone_quey_vector_creation import create_query_vector
from .pinecone_similarity_search import run_similarity_search

def process_pinecone():
    pc: Pinecone = init_pinecone()
    _switch_deletion_mode(pc)
    # _switch_upsertion_mode(pc)
    
    
def _switch_upsertion_mode(pc: Pinecone):
    index = upsert_data(pc)
    embedding_data = create_query_vector(pc)
    run_similarity_search(index, embedding_data)
    
def _switch_deletion_mode(pc: Pinecone):
    delete_index(pc)
    