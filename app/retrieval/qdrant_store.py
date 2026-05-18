from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct
)

from app.config.settings import *

client=QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT
)


def create_collection(
        dim=384):

    collections=client.get_collections()

    names=[
        c.name
        for c
        in collections.collections
    ]

    if COLLECTION_NAME not in names:

        client.create_collection(
            collection_name=
            COLLECTION_NAME,

            vectors_config=
            VectorParams(
                size=dim,
                distance=
                Distance.COSINE
            )
        )


def insert_chunks(
        embeddings,
        chunks):

    points=[]

    for idx,(vector,text) in enumerate(
            zip(
                embeddings,
                chunks
            )
    ):

        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={
                    "text":text
                }
            )
        )

    client.upsert(
        collection_name=
        COLLECTION_NAME,

        points=points
    )


def search(
        embedding,
        top_k=20
):

    result=client.search(
        collection_name=
        COLLECTION_NAME,

        query_vector=
        embedding,

        limit=top_k
    )

    return [

        item.payload["text"]

        for item

        in result
    ]