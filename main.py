from memory.recall import RecallMemory
from memory.archival import ArchivalMemory
from context.main_context import update_main_context
from utils.embedding import generate_embedding

recall_memory = RecallMemory()
archival_memory = ArchivalMemory()
main_context = ""

query = "Explain memory systems in AI."

# fetch from recall memory
recall_snippet = recall_memory.fetch_memory()
if recall_snippet:
    main_context = update_main_context(main_context, f"Recall Memory:\n{recall_snippet}")

# query archival memory if recall memory is insufficient
query_embedding = generate_embedding(query)
archival_results = archival_memory.query_memory(query_embedding)
if archival_results:
    main_context = update_main_context(main_context, f"Archival Memory:\n{archival_results[0]}")

# update main context with user query
main_context = update_main_context(main_context, f"User: {query}")

print(main_context)
