from typing import List

from datetime import datetime

from pydantic import BaseModel

class PersonRequest(BaseModel):

    count: int
    waiting_time: int


class Person(BaseModel):

    first_name: str
    birthdate: datetime
    gender: str

class PersonResponse(BaseModel):

    items: List[Person]
