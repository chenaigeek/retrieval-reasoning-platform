from app.embeddings.encoder import (
    generate_embeddings
)

from app.retrieval.qdrant_store import (
    search
)

from app.ranking.reranker import (
    rerank
)


async def retrieve_context(
        query:str
):

    embedding=generate_embeddings(
        [query]
    )[0]

    retrieved_docs=search(
        embedding,
        top_k=20
    )

    reranked=rerank(
        query=query,
        documents=
        retrieved_docs,
        top_k=5
    )

    context=[]

    for item in reranked:

        context.append(
            item["text"]
        )

    return "\n".join(
        context
    )