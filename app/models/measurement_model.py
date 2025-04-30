import sqlalchemy
import os
from sqlmodel import SQLModel, Field, Column
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from datetime import datetime
from .utils import MEASUREMENT_TYPE

class Measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    measurement_type: MEASUREMENT_TYPE
    value: float | None = Field(sa_column=Column(
        EncryptedType(sqlalchemy.Unicode,
                      os.getenv("DATA_ENCRYPTION_KEY"),
                      AesEngine,
                      'pkcs5')))
    measured_at: datetime | None = Field(index=True)
    created_at: int | None = Field(index=True)