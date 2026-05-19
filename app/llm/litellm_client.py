from litellm import acompletion

from app.monitoring.metrics import TOKEN_USAGE
from app.routing.ray_router import route_request


async def llm_call(prompt:str):

    # Dynamically select model based on query complexity
    model = ray.get(
        route_request.remote(prompt)
    )

    response = await acompletion(
        model=model,
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    usage = response.usage.total_tokens if response.usage else 0

    TOKEN_USAGE.inc(usage)

    return {
        "content":response.choices[0].message.content,
        "token_count":usage,
        "model":model
    }