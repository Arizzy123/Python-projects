name= input("What is your name? ")
print("Welcome", name, "to this adventure game! ")

question = input("You are on a nowhere land where you do not know which way to go. Will you like to go left or right?")

if question == "left":
    question == input("You come to a river, you can walk around it or swim across? Type walk to walk and swim to swim? ")

    if question == "walk":
        print("You walked for many miles and were eaten by a lion and lost the game. ")

    elif question == "swim":
        print("You swam across and were eaten by a crocodile")

elif question == "right":
    question = input("You come to a bridge, it looks wobbly do you want to cross or go back ? ")

    if question ==  "back":
        print("You go back and lose.")
    elif question == "cross":
        question = input("You cross the bridge and meet a stranger. Do you want to talk to them or(yes/no)? ")

        if question == "yes":
            print(" You talk to the stranger and they give gold. YOU WIN! ")
        elif question == "no":
            print("You ignore the stranger and they are offended. YOU LOSE! ")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("THANK YOU FOR TRYING THE ADVENTURE GAME", name,)