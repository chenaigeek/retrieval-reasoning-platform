def hallucination_rate(response: str, context: str):

    response_words = set(response.lower().split())
    context_words = set(context.lower().split())

    unsupported = response_words - context_words

    return round(len(unsupported) / max(len(response_words), 1), 4)
