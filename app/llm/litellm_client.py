from litellm import acompletion

from app.config.settings import (
    AGENT_MODEL
)


async def llm_call(
        prompt:str
):

    response=await acompletion(

        model=
        AGENT_MODEL,

        messages=[

            {
                "role":"user",
                "content":prompt
            }

        ]
    )

    return (

        response
        .choices[0]
        .message
        .content
    )