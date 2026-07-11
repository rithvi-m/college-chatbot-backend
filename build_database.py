import json
from fastembed import TextEmbedding
from prepare_data import college_knowledge

print("Loading embedding model...")
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

print("Converting text to embeddings...")
data = []
for item in college_knowledge:
    embedding = list(model.embed([item["text"]]))[0].tolist()
    data.append({
        "id": item["id"],
        "text": item["text"],
        "embedding": embedding
    })

with open("embeddings.json", "w") as f:
    json.dump(data, f)

print(f"Done! Saved {len(data)} chunks to embeddings.json")
