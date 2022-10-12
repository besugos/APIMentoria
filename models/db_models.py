from sqlalchemy import Column, Integer, String, Date, Time, Boolean


class Employee():
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    cpf = Column(String)
    email = Column(String)
    password = Column(String)
    zipcode = Column(String)
    birthdate = Column(Date)
    street = Column(String)
    number = Column(String)
    district = Column(String)
    city = Column(String)
    state = Column(String)
    children_amount = Column(Integer)
    children_names = Column(String)
    marital_status = Column(String)


class Dayoff():
    __tablename__ = 'dayoff'

    dayoff_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(Date)
    type = Column(String)
    start = Column(Time)
    end = Column(Time)
    communicated_peers = Column(Boolean)
    communicated_team = Column(Boolean)
    communicated_manager = Column(Boolean)
    has_substitute = Column(Boolean)
    substitute = Column(String)
    pending_work = Column(String)
