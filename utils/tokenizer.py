from transformers import GPT2TokenizerFast


def count_tokens(text: str) -> int:
    """Count the number of tokens in a text."""
    return len(text.split()) # space-based tokenization
