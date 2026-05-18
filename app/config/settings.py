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