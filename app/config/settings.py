from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

QDRANT_HOST=os.getenv("QDRANT_HOST")
QDRANT_PORT=int(
    os.getenv("QDRANT_PORT")
)

EMBEDDING_MODEL=os.getenv(
    "EMBEDDING_MODEL"
)

COLLECTION_NAME=os.getenv(
    "COLLECTION_NAME"
)
RERANKER_MODEL=os.getenv(
    "RERANKER_MODEL"
)
AGENT_MODEL=os.getenv(
    "AGENT_MODEL"
)
REDIS_HOST=os.getenv(
    "REDIS_HOST"
)

REDIS_PORT=int(
    os.getenv(
        "REDIS_PORT"
    )
)

POSTGRES_USER=os.getenv(
    "POSTGRES_USER"
)

POSTGRES_PASSWORD=os.getenv(
    "POSTGRES_PASSWORD"
)

POSTGRES_HOST=os.getenv(
    "POSTGRES_HOST"
)

POSTGRES_PORT=os.getenv(
    "POSTGRES_PORT"
)

POSTGRES_DB=os.getenv(
    "POSTGRES_DB"
)

LANGCHAIN_API_KEY=os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2=os.getenv("LANGCHAIN_TRACING_V2")
LANGCHAIN_PROJECT=os.getenv("LANGCHAIN_PROJECT")
OTEL_SERVICE_NAME=os.getenv("OTEL_SERVICE_NAME")
AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION=os.getenv("AWS_REGION")
S3_BUCKET=os.getenv("S3_BUCKET")