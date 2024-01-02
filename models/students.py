from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    home_address = Column(String)
    group_id = Column(Integer, ForeignKey("groups.id"))

    def __init__(self, name: str, surname: str, age: int, home_address: str, gr_id: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.home_address = home_address
        self.group_id = gr_id

# students
# id | name | surname | age | home_address | group_id |
#  1 | fff  | sfsdfgs |  13 | Lviv         |    1     |
#  2 | ff1  | sfsdfg2 |  13 | Lviv         |    2     |


# groups
# id | name_of_group |
# 1  | Python group  |
# 2  | Python group2 |
