from sqlalchemy import Column, String, Integer, ForeignKey, Table

from sqlalchemy.orm import relationship
from models.database import Base


table_relationship = Table(
    "relationsip_between_tables",
    Base.metadata,
    Column("subject_id", Integer, ForeignKey("subjects.id")),
    Column("group_id", Integer, ForeignKey("groups.id"))
)


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    groups = relationship("Group", secondary=table_relationship, backref="group_sublect")

    def __repr__(self):
        return f"Subject ID - {self.id} with Name - {self.title}"


# relationsip_between_tables
# subject_id | group_id |
#    1       |    1
#    1       |    2
#    1       |    3
#    1       |    4
#    2       |    1
#    2       |    2
#    3       |    4
#    3       |    2

# subjects
# id | title | groups |
# 1  | Math  | 1      |
# 2  | Eng   | 1      |
# 3  | Ukr   | 1      |

# groups
# id | name_of_group |
# 1  |  6-A          |
# 2  | 7-A           |
# 3  | 11-B          |
# 4  | 8-C           |