import time

from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase

from app.monitoring.evaluator import hallucination_rate

faithfulness_metric = FaithfulnessMetric()

# Example pricing estimate; replace with actual model pricing later
TOKEN_COST = 0.000002


def estimate_cost(token_count):
    return round(token_count * TOKEN_COST, 6)


async def evaluate_sample(question, answer, context, ground_truth):

    start = time.time()

    # DeepEval checks whether generated output is supported by retrieved context
    test_case = LLMTestCase(
        input=question,
        actual_output=answer,
        expected_output=ground_truth,
        retrieval_context=[context],
    )

    faithfulness_metric.measure(test_case)

    latency = time.time() - start

    # Approximate token count for now
    # Later we can replace this with actual LiteLLM/OpenAI usage data
    token_count = len((question + answer + context).split())

    return {
        "faithfulness": round(faithfulness_metric.score, 4),
        "hallucination_rate": hallucination_rate(answer, context),
        "latency": round(latency, 4),
        "cost": estimate_cost(token_count),
    }
