import os

from mongoengine import connect
from mongoengine.connection import get_connection


def connect_db():
    try:
        get_connection()
        return
    except Exception:
        pass

    connect(
        db=os.getenv("DB_NAME", "blogdb"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "27017")),
        uuidRepresentation="standard",
    )
