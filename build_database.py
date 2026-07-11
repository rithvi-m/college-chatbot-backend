from fastembed import TextEmbedding
import chromadb
from prepare_data import college_knowledge

print("Loading embedding model... (this may take 20-30 seconds the first time)")
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

print("Setting up ChromaDB...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="college_info")

print("Converting text to embeddings and storing...")
for item in college_knowledge:
    embedding = list(model.embed([item["text"]]))[0].tolist()
    collection.upsert(
        ids=[item["id"]],
        embeddings=[embedding],
        documents=[item["text"]]
    )

print(f"Done! Stored {len(college_knowledge)} chunks in the database.")
print(f"Total items in collection: {collection.count()}")