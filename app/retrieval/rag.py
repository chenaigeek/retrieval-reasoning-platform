from app.embeddings.encoder import (
    generate_embeddings
)

from app.retrieval.qdrant_store import (
    search
)

async def retrieve_context(
        query:str):

    embedding=generate_embeddings(
        [query]
    )[0]

    docs=search(
        embedding,
        top_k=5
    )

    return "\n".join(
        docs
    )