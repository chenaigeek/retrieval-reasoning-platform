from sentence_transformers import SentenceTransformer
from app.config.settings import EMBEDDING_MODEL

model = SentenceTransformer(
    EMBEDDING_MODEL
)

def generate_embeddings(texts:list):

    return model.encode(
        texts,
        normalize_embeddings=True
    ).tolist()