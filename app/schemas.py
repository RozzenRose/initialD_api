from pydantic import BaseModel, field_validator, PositiveFloat
from datetime import date
from pydantic.v1 import root_validator, validator


class CreateUser(BaseModel):
    email: str
    password: str