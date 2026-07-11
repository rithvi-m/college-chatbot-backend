from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="college_info")

def search(question, top_n=2):
    question_embedding = model.encode(question).tolist()
    
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_n
    )
    
    return results["documents"][0]

# Try it out
question = "how much does it cost to study here"
print(f"Question: {question}\n")

matches = search(question)
for i, text in enumerate(matches):
    print(f"Match {i+1}: {text}\n")