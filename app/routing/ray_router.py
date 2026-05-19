import ray

from app.routing.model_router import select_model

ray.init(ignore_reinit_error=True)


@ray.remote
def route_request(query: str):
    return select_model(query)
