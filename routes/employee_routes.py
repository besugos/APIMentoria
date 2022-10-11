from fastapi import APIRouter

from models.models import Employee

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
async def create_employee(employee: Employee):
    return {"msg": "create employee route"}

