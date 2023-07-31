import sqlite3

def action():
    action_input=input("What will you like to do? ")
    return action_input

def register():
    print("REGISTER")
    username_input=input('enter your username: ')
    password_input= input('enter your password: ')
    email_input= input('enter your e-mail: ')

    connection=sqlite3.connect('users.db')
    cursor= connection.cursor()
    cursor.execute(f"INSERT INTO users VALUES ('{username_input}','{password_input}','{email_input}')")
    print("REGISTRATION SUCCESSFUL")

    connection.commit()
    connection.close()

def login():
    print('LOGIN')
    username_input= input("enter your username: ")
    password_input= input("enter your password: ")

    connection=sqlite3.connect('users.db')
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM users")
    all_users= cursor.fetchall()

    all_users_details=[]
    for each_user_detail in all_users:
        each_user=[]
        for item in each_user_detail:
            each_user.append(str(item))
            all_users_details+= each_user




    if str(password_input) in all_users_details:
        if str(username_input) in all_users_details:
            return "LOGIN SUCCESSFUL"
        else:
            return "INVALID USERNAME"

    else:
        return "Authentication Unsuccessful"

    connection.commit()
    connection.close()

main_action_input= action()
if main_action_input.upper() == "REGISTER":
    print(register())

elif main_action_input.upper() == "LOGIN":
    print(login())
else:
    action()

# connection=sqlite3.connect('users.db')
# cursor=connection.cursor()
# cursor.execute("""CREATE TABLE users(
#     username_input text,
#     password_input text,
#     e-mail_input text
#
# )
# """)
# connection.commit()
# connection.close()


