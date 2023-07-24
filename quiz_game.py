print("Welcome to Ridwan game! ")

name=input("What is your name? ")

Age=int(input("How many years are you? "))
if Age<=15:
    print("Okay")
else:
    print("You are not qualified for this game ")
    quit()


playing=input("Will you like to play this game? ")

if playing.lower() !="yes":
    quit()

print("Okay! let play the game ")
score=0

answer=input("What does CPU means? ").lower()
if answer=="central processing unit":
    print("Congrats, you are correct ")
    score+=1
else:
    print("Incorrect")

answer=input("What does VDU means? ")
if answer.lower() =="visual display unit":
    print("Congrats, you are correct ")
    score+=1
else:
    print("Incorrect")

answer=input("How many days are there in month February? ")
if answer=="28":
    print("Congrats, you are correct ")
    score+=1
else:
    print("Incorrect ")

answer=input("What does RAM means? ")
if answer.lower() =="random access memory":
    print("Congrats, you are correct ")
    score += 2
else:
    print("Incorrect ")

answer=input("What does ROM means? ")
if answer=="read only memory":
    print("Congrats, you are correct ")
    score += 1
else:
    print("Incorrect ")

print("Congrats you got " +  str(score)+ " questions correct")
print("Congrats you got " +  str((score/5) * 100)+ " questions correct")