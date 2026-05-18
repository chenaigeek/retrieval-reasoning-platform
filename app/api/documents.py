from fastapi import (
    APIRouter,
    UploadFile
)

from app.services.document_loader import (
    load_pdf,
    load_text
)

from app.retrieval.chunker import (
    chunk_text
)

from app.embeddings.encoder import (
    generate_embeddings
)

from app.retrieval.qdrant_store import (
    create_collection,
    insert_chunks
)

router=APIRouter()

create_collection()


@router.post(
    "/upload"
)
async def upload_document(
        file:UploadFile):

    content=await file.read()

    if file.filename.endswith(
            ".pdf"
    ):
        text=load_pdf(
            file.file
        )

    else:
        text=load_text(
            content
        )

    chunks=chunk_text(
        text
    )

    embeddings=generate_embeddings(
        chunks
    )

    insert_chunks(
        embeddings,
        chunks
    )

    return {

        "chunks":
        len(chunks),

        "status":
        "uploaded"
    }