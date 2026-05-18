from fastapi import FastAPI
from app.api.chat import router

app = FastAPI(
    title="LLM Platform"
)

app.include_router(router)