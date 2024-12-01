# Mini-Letta

Mini-Letta is a lightweight implementation inspired by Letta's memory-augmented system. It introduces a hierarchical memory system to extend the context capabilities of language models. The system has three main components:

- **Main Context**: The active window of conversation with the language model.
- **Recall Memory**: Session-specific memory for frequently accessed or transient data.
- **Archival Memory**: Long-term memory for persistent data stored using embeddings.

---

## Features

- **Main Context Management**: Dynamically updates and maintains a fixed token-limited context.
- **Recall Memory**: Stores session-relevant facts for quick access.
- **Archival Memory**: Supports long-term storage and similarity-based retrieval with embeddings.
- **Tokenization**: Ensures the context remains within the maximum token limit.
- **Embedding Generation**: Uses pre-trained models to generate text embeddings.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ManishMothi/mini-letta.git
   cd mini-letta
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the application:

```bash
python main.py
```

### Example Workflow

- The system dynamically builds and maintains the **main context**.
- **Recall memory** is used to store and retrieve session-specific details.
- **Archival memory** enables similarity-based queries for long-term knowledge.

The output is a fully enriched context ready to send to a language model.

---

## Configuration

You can modify the settings in `config.py`:

```python
MAX_TOKENS = 1000  # Maximum tokens in the main context
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
VECTOR_DB_NAME = "archival_memory"
```

---

## Dependencies

- Python 3.9 or later
- NumPy `<2.0`
- Sentence Transformers
- PyTorch
- ChromaDB

To install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
mini_letta/
│
├── main.py            # Entry point
├── memory/
│   ├── recall.py      # Recall memory logic
│   ├── archival.py    # Archival memory logic
├── context/
│   ├── main_context.py# Main context logic
├── utils/
│   ├── tokenizer.py   # Tokenization functions
│   ├── embedding.py   # Embedding generation
├── config.py          # Configuration settings
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

---

## Future Enhancements

- Add integration with LLM APIs (e.g., OpenAI GPT or Hugging Face models).
- Implement rules for prioritizing which memory to update.
- Explore cloud-based solutions for long-term archival memory storage.
