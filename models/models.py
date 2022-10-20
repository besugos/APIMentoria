from typing import Union

from pydantic import BaseModel
from pydantic.schema import datetime, time, date
from pydantic.types import date


class Employee(BaseModel):
    employee_id: int = None
    first_name: str
    last_name: str
    cpf: str
    email: str
    password: str
    zipcode: str
    birthdate: date
    street: str
    number: str
    district: str
    city: str
    state: str
    children_amount: int
    children_names: str
    marital_status: str

    class Config:
        orm_mode = True


class Dayoff(BaseModel):
    dayoff_id: int = None
    employee_id: int
    date: date
    type: str
    start: time
    end: time
    communicated_peers: bool
    communicated_team: bool
    communicated_manager: bool
    has_substitute: bool
    substitute: str
    pending_work: str

    class Config:
        orm_mode = True


class User(BaseModel):
    email: str
    password: str
