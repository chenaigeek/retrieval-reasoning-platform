from fastapi import FastAPI

from app.api.chat import (
    router as chat_router
)

from app.api.documents import (
    router as doc_router
)
from app.api.agents import (
    router as agent_router
)


from app.api.evaluation import (
    router as eval_router
)
from app.middleware.observability import ObservabilityMiddleware
from app.api.monitoring import router as monitoring_router
from app.api.evaluation import router as evaluation_router


app=FastAPI()

app.include_router(
    chat_router
)

app.include_router(
    doc_router
)

app.include_router(
    eval_router
)
app.include_router(
    agent_router
)


app.add_middleware(ObservabilityMiddleware)
app.include_router(monitoring_router)
app.include_router(evaluation_router)
