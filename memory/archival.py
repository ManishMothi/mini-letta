from chromadb import Client
from config import VECTOR_DB_NAME

class ArchivalMemory:
    def __init__(self):
        self.client = Client()
        self.collection = self.client.create_collection(name=VECTOR_DB_NAME) 
    
    def add_entry(self, embedding, metadata):
        '''
        add an entry into archival memory.
        '''
        self.collection.add(embeddings=[embedding], metadata=[metadata], ids=[str(len(self.collection))])

    def query_memory(self, query_embedding, n_results = 1):
        '''
        retrieve top n_results most relevant entries from archival memory. 
        '''
        results = self.collection.query(query_embeddings=[query_embedding], n_results=n_results)
        return results['metadatas']

