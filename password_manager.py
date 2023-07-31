password = input("What is the master password? ")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            print("User:", user, "Password:", passw)

def add():
    name = input("Account name: ")
    password = input("password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + password + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ")
    if mode == "q":
        breaks

    if mode == "view":
        view()
    elif mode == "add":
        add()