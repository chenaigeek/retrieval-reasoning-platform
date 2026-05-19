import json


def load_dataset(path="data/eval_questions.json"):
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)