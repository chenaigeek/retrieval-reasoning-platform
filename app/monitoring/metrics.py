from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter("requests_total", "Total requests")
FAILURE_COUNT = Counter("failures_total", "Failures")

LATENCY = Histogram("request_latency_seconds", "Latency")
TOKEN_USAGE = Counter("token_usage_total", "Total tokens")

ACTIVE_REQUESTS = Gauge("active_requests", "Active requests")
