from fastapi import APIRouter, UploadFile

from app.services.document_loader import load_pdf, load_text

from app.retrieval.chunker import chunk_text

from app.embeddings.encoder import generate_embeddings

from app.retrieval.qdrant_store import create_collection, insert_chunks
from app.storage.s3_service import upload_file

router = APIRouter()

create_collection()


@router.post("/upload")
async def upload_document(file: UploadFile):

    content = await file.read()

    # Persist uploaded files to cloud storage
    file_key = await upload_file(content, file.filename)

    if file.filename.endswith(".pdf"):
        text = load_pdf(file.file)
    else:
        text = load_text(content)

    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    insert_chunks(embeddings, chunks)

    return {"status": "uploaded", "chunks": len(chunks), "s3_key": file_key}
