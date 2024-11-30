'''
The context/ folder manages main context, which refers to the active data that is directly passed to the language model (LLM).
This data exists in the current context window and is continually updated as the conversation progresses.

Responsibilities:
Manage the current session's active context.
Handle updates, truncations, and token limits for the main context string.
Ensure the LLM is fed only the most relevant and recent information within its token limit.


The context is transient and session-specific—it exists only as long as the session or conversation is active.
The context/ folder focuses on organizing the active data fed to the LLM.
'''