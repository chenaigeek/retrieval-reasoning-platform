from fastapi import APIRouter
from prometheus_client import generate_latest
from fastapi.responses import PlainTextResponse

router=APIRouter()


@router.get("/metrics")
async def metrics():
    return PlainTextResponse(generate_latest())