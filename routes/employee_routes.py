from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from persistency.employee_persistency import EmployeePersistency
from models.models import Employee
from persistency.persistency_utils import get_db, create_db

create_db()

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_employees():
    return {"msg": "get all employees route"}


@router.get("/{id}")
async def get_employee_by_id():
    return {"msg": "get employee by id route"}


@router.post("/")
async def create_employee(employee: Employee, db: Session = Depends(get_db)):
    created_employee = EmployeePersistency(db).create(employee)
    return created_employee

