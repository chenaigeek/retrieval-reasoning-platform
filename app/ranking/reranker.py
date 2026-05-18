from sentence_transformers import CrossEncoder

from app.config.settings import (
    RERANKER_MODEL
)

model=CrossEncoder(
    RERANKER_MODEL
)


def rerank(
        query:str,
        documents:list,
        top_k=5
):

    pairs=[]

    for doc in documents:

        pairs.append(
            [query,doc]
        )

    scores=model.predict(
        pairs
    )

    results=[]

    for doc,score in zip(
            documents,
            scores
    ):

        results.append(
            {
                "text":doc,
                "score":float(score)
            }
        )

    ranked=sorted(
        results,
        key=lambda x:x["score"],
        reverse=True
    )

    return ranked[:top_k]