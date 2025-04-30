import sqlalchemy
import os
from sqlmodel import SQLModel, Field, Column
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    login_id: str = Field(index=True)
    passwd: str = Field(default=None, exclude=True)
    name: str
    rrn: str = Field(sa_column=Column(
        EncryptedType(sqlalchemy.Unicode,
                      os.getenv("DATA_ENCRYPTION_KEY"),
                      AesEngine,
                      'pkcs5')))
    created_at: int | None = Field(index=True)
    access_token: str | None = None
