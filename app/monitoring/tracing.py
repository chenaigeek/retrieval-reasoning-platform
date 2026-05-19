from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from app.config.settings import OTEL_SERVICE_NAME

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(OTEL_SERVICE_NAME)
