import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.monitoring.metrics import *
from app.monitoring.tracing import tracer


class ObservabilityMiddleware(BaseHTTPMiddleware):

    async def dispatch(self,request,call_next):

        REQUEST_COUNT.inc()
        ACTIVE_REQUESTS.inc()

        start=time.time()

        with tracer.start_as_current_span(request.url.path):

            try:

                response=await call_next(request)

            except Exception:

                FAILURE_COUNT.inc()
                raise

        latency=time.time()-start

        LATENCY.observe(latency)

        ACTIVE_REQUESTS.dec()

        return response