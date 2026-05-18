from openai import AsyncOpenAI
from app.config.settings import OPENAI_API_KEY
from app.config.settings import MODEL_NAME

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)


async def generate_response(messages):

    response = await client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages
    )

    return response.choices[0].message.content


async def stream_response(messages):

    stream = await client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        stream=True
    )

    async for chunk in stream:

        content = chunk.choices[0].delta.content

        if content:
            yield content