import tiktoken

encoding=tiktoken.get_encoding(
    "cl100k_base"
)

def chunk_text(
        text:str,
        chunk_size=300,
        overlap=50):

    tokens=encoding.encode(
        text
    )

    chunks=[]

    start=0

    while start < len(tokens):

        end=start+chunk_size

        chunk_tokens=tokens[
            start:end
        ]

        chunk=encoding.decode(
            chunk_tokens
        )

        chunks.append(chunk)

        start+=(
            chunk_size-overlap
        )

    return chunks