import pandas as pd


def create_report(results):

    df=pd.DataFrame(results)

    report={
        "samples":len(df),
        "avg_faithfulness":round(df["faithfulness"].mean(),4),
        "avg_hallucination":round(df["hallucination_rate"].mean(),4),
        "avg_latency":round(df["latency"].mean(),4)
    }

    return report