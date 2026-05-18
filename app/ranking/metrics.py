def recall_at_k(
        relevant_docs,
        retrieved_docs,
        k=5
):

    top_docs=retrieved_docs[:k]

    hits=0

    for doc in relevant_docs:

        if doc in top_docs:
            hits+=1

    return hits/len(
        relevant_docs
    )


def mrr(
        relevant_docs,
        retrieved_docs
):

    for idx,doc in enumerate(
            retrieved_docs
    ):

        if doc in relevant_docs:

            return 1/(
                idx+1
            )

    return 0