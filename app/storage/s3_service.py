import uuid
import boto3
from app.config.settings import *

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


async def upload_file(content: bytes, filename: str):

    # Generate unique names to avoid collisions across distributed workers
    object_name = f"{uuid.uuid4()}-{filename}"

    s3.put_object(Bucket=S3_BUCKET, Key=object_name, Body=content)

    return object_name
