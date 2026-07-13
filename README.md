# College Chatbot – Backend

A RAG (Retrieval-Augmented Generation) based chatbot backend that answers college-related queries. Built with FastAPI, Groq's LLaMA model for generation, and Hugging Face's Inference API for embeddings.

**Live API:** [college-chatbot-backend-o6eg.onrender.com](https://college-chatbot-backend-o6eg.onrender.com)
**Frontend:** [rithvi-m.github.io/college-chatbot-frontend](https://rithvi-m.github.io/college-chatbot-frontend/)

## How it works

1. College information is split into chunks and converted into embeddings using the Hugging Face Inference API.
2. Embeddings are stored locally in `embeddings.json` (no external vector DB needed — similarity search runs on lightweight numpy cosine similarity).
3. When a user asks a question, the backend embeds the query, retrieves the most relevant chunks, and passes them as context to Groq's LLaMA model.
4. The model generates a natural-language answer grounded in the retrieved college information.

## Tech stack

- **Framework:** FastAPI + Uvicorn
- **LLM:** Groq API (LLaMA)
- **Embeddings:** Hugging Face Inference API
- **Similarity search:** NumPy cosine similarity (no ChromaDB/FAISS dependency)
- **Deployment:** Render

## Project structure

| File | Purpose |
|---|---|
| `main.py` | FastAPI app entry point — API routes and server startup |
| `rag_chat.py` | Core RAG logic — retrieval + prompt construction + LLM call |
| `build_database.py` | Builds/updates the embeddings database from source data |
| `prepare_data.py` | Cleans and prepares raw college data before embedding |
| `embeddings.json` | Precomputed embeddings used for retrieval |
| `test_search.py` | Tests for the retrieval/search logic |
| `requirements.txt` | Python dependencies |

## Setup

```bash
git clone https://github.com/rithvi-m/college-chatbot-backend.git
cd college-chatbot-backend
pip install -r requirements.txt
```

Create a `.env` file with your API keys:

```
GROQ_API_KEY=your_groq_api_key
HF_API_KEY=your_huggingface_api_key
```

Build the embeddings database (if not already present):

```bash
python build_database.py
```

Run the server locally:

```bash
uvicorn main:app --reload
```

## API

Send a POST request with a user query to get a context-grounded response from the chatbot. See `main.py` for exact endpoint routes and request/response schema.

## Notes

- Switched from ChromaDB to a lightweight NumPy-based similarity search to keep the app within free-tier memory limits on Render.
- Embeddings are generated via the Hugging Face Inference API rather than a local model, keeping the deployment footprint small.
