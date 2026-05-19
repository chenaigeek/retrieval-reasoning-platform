from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.schemas import ChatRequest
from app.llm.client import generate_response
from app.llm.client import stream_response

from app.memory.chat_store import add_message, get_history
from app.retrieval.rag import retrieve_context

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    context = await retrieve_context(request.message)

    prompt = f"""
Context:

{context}

Question:

{request.message}
"""

    add_message(request.session_id, "user", prompt)

    messages = get_history(request.session_id)

    response = await generate_response(messages)

    add_message(request.session_id, "assistant", response)

    return {"response": response}


@router.post("/stream")
async def stream_chat(request: ChatRequest):

    add_message(request.session_id, "user", request.message)

    messages = get_history(request.session_id)

    return StreamingResponse(stream_response(messages), media_type="text/plain")
