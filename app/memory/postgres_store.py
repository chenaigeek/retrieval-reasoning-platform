from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import (
    declarative_base
)

Base=declarative_base()


class Conversation(
        Base
):

    __tablename__="conversation"

    id=Column(
        Integer,
        primary_key=True
    )

    session_id=Column(
        String
    )

    role=Column(
        String
    )

    content=Column(
        Text
    )