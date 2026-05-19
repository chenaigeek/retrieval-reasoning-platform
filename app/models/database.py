from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import *

DATABASE_URL = f"""

postgresql://
{POSTGRES_USER}:
{POSTGRES_PASSWORD}@
{POSTGRES_HOST}:
{POSTGRES_PORT}/
{POSTGRES_DB}

""".replace("\n", "")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
