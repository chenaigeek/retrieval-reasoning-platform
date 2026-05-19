import re


def classify_query(query:str):

    # Heuristic complexity scoring
    score = 0

    if len(query.split()) > 20:
        score += 1

    reasoning_words = [
        "compare",
        "analyze",
        "reason",
        "evaluate",
        "explain why",
        "tradeoff"
    ]

    if any(word in query.lower() for word in reasoning_words):
        score += 1

    if len(re.findall(r"\?",query)) > 1:
        score += 1

    return "large" if score >= 2 else "small"