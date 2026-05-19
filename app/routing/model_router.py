from app.routing.classifier import classify_query
from app.config.settings import SMALL_MODEL, LARGE_MODEL


def select_model(query: str):

    model_size = classify_query(query)

    # Route harder reasoning tasks to stronger models
    if model_size == "large":
        return LARGE_MODEL

    return SMALL_MODEL
