import time
from db import Task, User, engine, sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class Users:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.login_suscess = 0

    def write_to_db_user_password(self) -> None:
        taskss = session.query(User).all()
        for task in taskss:
            if self.username == task.username:
                return print("Username already exist, please login")
        else:
            task_to_db2 = User(username = self.username, password = self.password)
            session.add(task_to_db2)
            session.commit() 
        return print(f"{self.username} are registered!!!") 

    def check_login(self) -> str:
        taskss = session.query(User).all()
        for task in taskss:
            if self.username == task.username and self.password == task.password:
                login_suscess = task.username
                return login_suscess
        else:
            return False
    
    @staticmethod
    def get_all_task(input_user) -> None:
        time.sleep(0.2)
        print("*************")
        get_user_task = session.query(User).filter_by(username = input_user).first()
        for number, task in enumerate(get_user_task.tasks, start=1):
            print(f"{number} - {task}")
        time.sleep(0.2)
        print("*************")

    @staticmethod
    def write_task_to_db(task_from_user: str, input_username: str) -> None:
        user1 = session.query(User).filter_by(username = input_username).first()
        user1.tasks.append(Task(task = task_from_user))
        session.add(user1)
        session.commit()

    @staticmethod
    def update_task(update_task_by_id: str, update_task: str) -> None:
        update_row = session.query(Task).filter_by(id = update_task_by_id).one()
        update_row.task = update_task
        session.commit()
        print(f"Task ID: {update_task} was updated!!!")

    @staticmethod
    def delete_task(del_task_by_id: str) -> None:
        delete_row = session.query(Task).filter_by(id = del_task_by_id).one()
        session.delete(delete_row)
        session.commit()
        print(f"ask ID: {del_task_by_id} was deleted!!!")


if __name__ == "__main__":
    pass