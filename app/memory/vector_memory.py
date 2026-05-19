from app.embeddings.encoder import generate_embeddings

from app.retrieval.qdrant_store import search


async def get_memory(query):

    embedding = generate_embeddings([query])[0]

    memory = search(embedding, top_k=3)

    return "\n".join(memory)
