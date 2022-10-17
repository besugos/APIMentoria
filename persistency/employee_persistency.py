from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from models import models, db_models


class EmployeePersistency():

    def __init__(self, db: Session):
        self.db = db

    def create(self, employee: models.Employee):
        db_employee = db_models.Employee(first_name=employee.first_name,
                                         last_name=employee.last_name,
                                         cpf=employee.cpf,
                                         email=employee.email,
                                         password=employee.password,
                                         zipcode=employee.zipcode,
                                         birthdate=employee.birthdate,
                                         street=employee.street,
                                         number=employee.number,
                                         district=employee.district,
                                         city=employee.city,
                                         state=employee.state,
                                         children_amount=employee.children_amount,
                                         children_names=employee.children_names,
                                         marital_status=employee.marital_status)
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee

    def read(self):
        employees = self.db.query(db_models.Employee).all()
        return employees

    def read_by_id(self, employee_id: int):
        statement = select(db_models.Employee).filter_by(employee_id=employee_id)
        employee = self.db.execute(statement).one()
        return employee

    def patch(self, employee: models.Employee):
        update_stmt = update(db_models.Employee).where(db_models.Employee.employee_id == employee.employee_id).values(
            first_name=employee.first_name,
            last_name=employee.last_name,
            cpf=employee.cpf,
            email=employee.email,
            password=employee.password,
            zipcode=employee.zipcode,
            birthdate=employee.birthdate,
            street=employee.street,
            number=employee.number,
            district=employee.district,
            city=employee.city,
            state=employee.state,
            children_amount=employee.children_amount,
            children_names=employee.children_names,
            marital_status=employee.marital_status)
        self.db.execute(update_stmt)
        self.db.commit()

    def delete(self, employee_id: int):
        statement = delete(db_models.Employee).where(db_models.Employee.employee_id == employee_id)
        self.db.execute(statement)
        self.db.commit()
