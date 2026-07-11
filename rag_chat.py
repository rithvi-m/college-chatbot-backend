import os
import json
import numpy as np
from dotenv import load_dotenv
from fastembed import TextEmbedding
from groq import Groq

load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

with open("embeddings.json", "r") as f:
    knowledge_data = json.load(f)


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve(question, top_n=2):
    question_embedding = list(model.embed([question]))[0].tolist()

    scored = []
    for item in knowledge_data:
        score = cosine_similarity(question_embedding, item["embedding"])
        scored.append((score, item["text"]))

    scored.sort(key=lambda x: x[0], reverse=True)
    top_matches = [text for score, text in scored[:top_n]]
    return top_matches


def ask_ai(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""You are a helpful assistant for Nehru Arts and Science College (NASC).
Answer the student''s question using ONLY the information below.
If the information doesn''t answer the question, say you don''t have that detail and suggest contacting the college office.
Keep your answer short and friendly, like a chat message.

College Information:
{context}

Student''s Question: {question}

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


if __name__ == "__main__":
    q = "how much does it cost to study here"
    print(f"Question: {q}\n")
    print(f"Answer: {get_answer(q)}")
