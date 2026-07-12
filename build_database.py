import os
import json
import requests
from dotenv import load_dotenv
from prepare_data import college_knowledge

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
HF_API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"


def get_embedding(text):
    response = requests.post(
        HF_API_URL,
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": text, "options": {"wait_for_model": True}}
    )
    return response.json()


print("Converting text to embeddings via Hugging Face API...")
data = []
for item in college_knowledge:
    embedding = get_embedding(item["text"])
    data.append({
        "id": item["id"],
        "text": item["text"],
        "embedding": embedding
    })
    print(f"- {item['id']} done")

with open("embeddings.json", "w") as f:
    json.dump(data, f)

print(f"Done! Saved {len(data)} chunks to embeddings.json")
