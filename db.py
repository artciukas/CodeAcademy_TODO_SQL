from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# create the database engine
engine = create_engine('sqlite:///todo.db', echo=False)
# create a base class for our model
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column("username", String, unique=True)
    password = Column("password", String)
    tasks = relationship("Task")

    def __repr__(self):
        return f"<Todo id={self.id}, user={self.username} task='{self.password}'>"

    # define a model for our todos table
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column("task", String)
    username_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", overlaps="tasks")

    def __repr__(self):
        return f"{self.task}(id-{self.id})"

# create the todos table
Base.metadata.create_all(engine)