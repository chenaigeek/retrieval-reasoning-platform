from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from app.ranking.metrics import (
    recall_at_k,
    mrr
)

router=APIRouter()


class EvaluationRequest(
    BaseModel
):

    relevant_docs:list

    retrieved_docs:list


@router.post(
    "/evaluate"
)
async def evaluate(
        request:
        EvaluationRequest
):

    recall=recall_at_k(

        request.relevant_docs,

        request.retrieved_docs,

        k=5
    )

    mrr_score=mrr(

        request.relevant_docs,

        request.retrieved_docs
    )

    return {

        "Recall@5":
        recall,

        "MRR":
        mrr_score
    }