from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.base import Engine
from sqlalchemy_utils import database_exists, create_database

from .model import DataModel, Base


class DatabaseInterfase:

    def __init__(self, user: str, passwd: str, host: str, port: int, db_name: str):
        self.__user = user
        self.__passwd = passwd
        self.__host = host
        self.__port = port
        self.__db_name = db_name
        self.__engine = self.__get_engine()

        self.__session = Session(bind=self.__engine)


    def __get_engine(self) -> Engine:
        url = f"postgresql://{self.__user}:{self.__passwd}@{self.__host}:{self.__port}/{self.__db_name}"
        if not database_exists(url):
            create_database(url)
        return create_engine(url)


    def insert_data(self, data: dict):
        new_data = DataModel(
            unsorted_seq = data['unsorted'],
            sorted_seq = data['sorted']
        )

        self.__session.add(new_data)
        self.__session.commit()


    def find_by_hash(self, _hash: str) -> str | None:
        data = self.__session.query(DataModel).filter(DataModel.unsorted_seq == _hash).all()
        if data:
            return [item.to_str() for item in data][0]
        return None


    def create_tables(self):
        Base.metadata.create_all(self.__engine)


    def drop_table(self):
        DataModel.__table__.drop(self.__engine)
