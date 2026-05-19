from fastapi import APIRouter
from pydantic import BaseModel

from app.ranking.metrics import recall_at_k, mrr
from app.evaluation.dataset import load_dataset
from app.evaluation.evaluator import evaluate_sample
from app.evaluation.report import create_report
from app.agents.workflow import graph

router = APIRouter()


class EvaluationRequest(BaseModel):
    relevant_docs: list
    retrieved_docs: list


# Existing Milestone 3 retrieval metrics endpoint
@router.post("/evaluate")
async def evaluate(request: EvaluationRequest):

    recall = recall_at_k(request.relevant_docs, request.retrieved_docs, k=5)

    mrr_score = mrr(request.relevant_docs, request.retrieved_docs)

    return {"Recall@5": round(recall, 4), "MRR": round(mrr_score, 4)}


# Milestone 8: full LLM evaluation pipeline
@router.post("/evaluate/run")
async def run_evaluation():

    dataset = load_dataset()
    results = []

    for item in dataset:

        question = item["question"]
        truth = item["ground_truth"]

        # Execute full multi-agent workflow
        output = await graph.ainvoke({"query": question})

        answer = output["answer"]
        context = output.get("context", "")

        metrics = await evaluate_sample(
            question=question, answer=answer, context=context, ground_truth=truth
        )

        metrics["question"] = question
        results.append(metrics)

    return create_report(results)
