from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DataModel(Base):
    __tablename__ = 'sequences'

    id = Column('id', Integer(), primary_key=True, autoincrement=True)
    unsorted_seq = Column('unsorted', String(64))
    sorted_seq = Column('sorted', String(64))


    def to_str(self) -> str:
        return self.sorted_seq[1:-1]
