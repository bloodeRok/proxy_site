from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean

from . import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<User(" \
               f"id={self.id}, " \
               f"email={self.email}, " \
               f"username={self.username}, " \
               f"registered_at={self.registered_at}, " \
               f"hashed_password={self.hashed_password}, " \
               f"is_active={self.is_active}, " \
               f"is_superuser={self.is_superuser}, " \
               f"is_verified={self.is_verified}" \
               f")>"

    def __str__(self):
        return self.__repr__()
