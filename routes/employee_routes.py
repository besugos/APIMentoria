from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from persistency.employee_persistency import EmployeePersistency
from models.models import Employee
from persistency.persistency_utils import get_db, create_db

create_db()

router = APIRouter(
    prefix="/employees",
    tags=["Employee"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_employees(db: Session = Depends(get_db)):
    employees = EmployeePersistency(db).read()
    return employees


@router.get("/{employee_id}")
async def get_employee_by_id(employee_id: int,  db: Session = Depends(get_db)):
    employee = EmployeePersistency(db).read_by_id(employee_id)
    return employee


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_employee(employee: Employee, db: Session = Depends(get_db)):
    created_employee = EmployeePersistency(db).create(employee)
    return created_employee


@router.delete("/{employee_id}")
async def get_employee_by_id(employee_id: int,  db: Session = Depends(get_db)):
    employee = EmployeePersistency(db).delete(employee_id)
    return {"msg": "Deleted successfully"}
