from sqlalchemy import Column, Integer, String

from .database import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name_of_group = Column(String)