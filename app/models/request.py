from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP

from . import Base


class Request(Base):
    __tablename__ = "request"

    id = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP, default=datetime.utcnow)
    inn = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    fio = Column(String, nullable=False)
    office = Column(String, nullable=False)
    module = Column(String, nullable=False)

    def __repr__(self):
        return f"<Request(" \
               f"id={self.id}, " \
               f"date={self.date}, " \
               f"inn={self.inn}," \
               f"nickname={self.nickname}, " \
               f"fio={self.fio}," \
               f"office={self.office}, " \
               f"module={self.module}" \
               f")>"

    def __str__(self):
        return self.__repr__()
