from app.llm.litellm_client import (
    llm_call
)


async def planner_agent(
        state
):

    prompt=f"""

Break this question
into subtasks.

Question:

{state['query']}

"""

    task_plan=await llm_call(
        prompt
    )

    state["plan"]=task_plan

    return state