import time

from db_connection import Users

print("Welcome to task creator")
time.sleep(0.2)
while True:
    check_login = input("1 - register\n2 - login\n")
    match check_login:
        case "1":
            input_username = input("Enter login for registration: ")
            time.sleep(0.2)
            input_password = input("Enter password for registration: ")
            time.sleep(0.2)
            users = Users(username=input_username, password=input_password)
            users.write_to_db_user_password()

        case "2":
            input_username = input("Please enter login: ")
            time.sleep(0.2)
            input_password = input("Please enter password: ")
            time.sleep(0.2)
            users = Users(username=input_username, password=input_password)
            login_status = users.check_login()
            if login_status == False:
                time.sleep(0.2)
                print("Login or password is incorect!!!")
                continue
            else:
                break

        case other:
            time.sleep(0.2)
            print("Wrong command!!!")

print("*************")
time.sleep(0.2)
print(f"Welcome to {input_username} DODO\nYour task list are:")
time.sleep(0.2)


while True:
    Users.get_all_task(input_user = input_username)

    choice = input("1 - enter task\n2 - update task\n3 - delete task\n0 - exit\n")

    match choice:
        case '1':
            task_from_user = input("Plese enter task name: ")
            Users.write_task_to_db(task_from_user, input_username)

        case '2':
            update_task_by_id = input("Enter task ID to update: ") 
            update_task = input("Enter task to update: ")
            Users.update_task(update_task_by_id, update_task)

        case '3':
            del_task_by_id = input("Enter task ID to delete: ") 
            Users.delete_task(del_task_by_id)

        case '0':
            print(f"Goodbye {input_username}")
            break

        case other:
            print("Wrong command!!!")