from datetime import datetime
from http.client import HTTPException

from pydantic import BaseModel
from pydantic.v1 import validator


class DateSchema(BaseModel):
    date: str
