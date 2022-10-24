from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from models import models, db_models
from utils.authentication_utils import create_hash


class DayoffPersistency():

    def __init__(self, db: Session):
        self.db = db

    def create(self, dayoff: models.Dayoff):
        db_dayoff = db_models.Dayoff(date=dayoff.date,
                                     type=dayoff.type,
                                     start=dayoff.start,
                                     end=dayoff.end,
                                     communicated_peers=dayoff.communicated_peers,
                                     communicated_team=dayoff.communicated_team,
                                     communicated_manager=dayoff.communicated_manager,
                                     has_substitute=dayoff.has_substitute,
                                     substitute=dayoff.substitute,
                                     pending_work=dayoff.pending_work,
                                     employee_id=dayoff.employee_id
                                     )

        self.db.add(db_dayoff)
        self.db.commit()
        self.db.refresh(db_dayoff)
        return db_dayoff

    def read(self):
        dayoffs = self.db.query(db_models.Dayoff).all()
        return dayoffs

    def read_by_id(self, dayoff_id: int):
        statement = select(db_models.Dayoff).filter_by(dayoff_id=dayoff_id)
        dayoff = self.db.execute(statement).one()
        return dayoff

    def patch(self, dayoff: models.Dayoff, dayoff_id: int):
        update_stmt = update(db_models.Dayoff).where(db_models.Dayoff.dayoff_id == dayoff_id).values(date=dayoff.date,
                                                                                                     type=dayoff.type,
                                                                                                     start=dayoff.start,
                                                                                                     end=dayoff.end,
                                                                                                     communicated_peers=dayoff.communicated_peers,
                                                                                                     communicated_team=dayoff.communicated_team,
                                                                                                     communicated_manager=dayoff.communicated_manager,
                                                                                                     has_substitute=dayoff.has_substitute,
                                                                                                     substitute=dayoff.substitute,
                                                                                                     pending_work=dayoff.pending_work,
                                                                                                     employee_id=dayoff.employee_id
                                                                                                     )
        self.db.execute(update_stmt)
        self.db.commit()

    def delete(self, dayoff_id: int):
        statement = delete(db_models.Dayoff).where(db_models.Dayoff.dayoff_id == dayoff_id)
        self.db.execute(statement)
        self.db.commit()
