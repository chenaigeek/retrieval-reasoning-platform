from litellm import acompletion
from app.monitoring.metrics import TOKEN_USAGE
from app.config.settings import AGENT_MODEL


async def llm_call(prompt:str):

    response=await acompletion(
        model=AGENT_MODEL,
        messages=[{"role":"user","content":prompt}]
    )

    usage=response.usage.total_tokens if response.usage else 0

    TOKEN_USAGE.inc(usage)

    return response.choices[0].message.content