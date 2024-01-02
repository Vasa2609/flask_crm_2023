from sqlalchemy import Column,Integer, String
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(60), unique=True)
    password = Column(String(16))

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password