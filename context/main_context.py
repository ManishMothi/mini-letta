from utils.tokenizer import count_tokens
from config import MAX_TOKENS

MAX_TOKENS = 1000

def update_main_context(main_context: str, new_entry: str) -> str:
    '''
    update and truncate the main context to fit within the token limit.
    '''
    main_context += f"\n{new_entry}"
    if count_tokens(main_context) > MAX_TOKENS:
        # Truncate tokens to fit the max limit
        tokenized = main_context.split()  # Simple tokenization for now
        main_context = " ".join(tokenized[-MAX_TOKENS:])
    return main_context