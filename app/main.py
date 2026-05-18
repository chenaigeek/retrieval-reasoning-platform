from fastapi import FastAPI

from app.api.chat import (
    router as chat_router
)

from app.api.documents import (
    router as doc_router
)

app=FastAPI()

app.include_router(
    chat_router
)

app.include_router(
    doc_router
)

from app.api.evaluation import (
    router as eval_router
)

app.include_router(
    eval_router
)