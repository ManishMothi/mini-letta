'''
The memory/ folder handles longer-term storage of information, divided into:

Recall Memory: Session-specific but stored externally, often for reuse during the same session.

Archival Memory: Persistent, long-term storage, typically involving embeddings or vector databases for similarity-based retrieval.

Responsibilities:

Recall Memory:
Manage frequently accessed session-specific data in a lightweight dictionary or similar structure.
Store temporary "facts" relevant to the session (e.g., user preferences, ongoing project).

Archival Memory:
Store historical or long-term data that exceeds the scope of the session.
Use embedding-based similarity search to retrieve relevant context dynamically.


Memory is external to the main context and persists beyond a single session. 
The memory/ folder focuses on organizing data storage and retrieval mechanisms that extend the agent's knowledge.

'''