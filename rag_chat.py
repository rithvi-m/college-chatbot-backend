import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq

# Load the secret API key from .env
load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load embedding model + database (same as before)
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="college_info")


def retrieve(question, top_n=2):
    question_embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_n
    )
    return results["documents"][0]


def ask_ai(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""You are a helpful assistant for Nehru Arts and Science College (NASC).
Answer the student's question using ONLY the information below.
If the information doesn't answer the question, say you don't have that detail and suggest contacting the college office.
Keep your answer short and friendly, like a chat message.

College Information:
{context}

Student's Question: {question}

Answer:"""

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content


def get_answer(question):
    chunks = retrieve(question)
    answer = ask_ai(question, chunks)
    return answer


# Test it
if __name__ == "__main__":
    q = "how much does it cost to study here"
    print(f"Question: {q}\n")
    print(f"Answer: {get_answer(q)}")