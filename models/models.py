from typing import Union

from pydantic import BaseModel


class Employee(BaseModel):
    employee_id: int = None
    first_name: str


class Dayoff(BaseModel):
    dayoff_id: int = None
    employee_id: int