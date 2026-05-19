from app.llm.litellm_client import llm_call


async def critic_agent(state):

    prompt = f"""

Review retrieved
context.

Question:

{state['query']}

Context:

{state['context']}

Identify missing
information or
errors.

"""

    review = await llm_call(prompt)

    state["review"] = review

    return state
