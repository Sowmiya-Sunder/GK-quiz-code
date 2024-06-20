print("--------- WELCOME TO MY GK QUIZ GAME ----------")

a = input("Do you want to play this game (Answer yes or no) : ")
if a.lower().strip() != "yes":
    quit()

print("Okay! Let's play!")
score = 0
qn1 = input("What is the full form for CPU? ")
if qn1.lower().strip() == "central processing unit":
    print("Well done, You got one point!")
    score = score + 1
else:
    print("Sorry, Incorrect answer")

qn2 = input("Which part of human cells are known as the powerhouse of the cell? ")
if qn2.lower().strip() == "mitochondria":
    print("Well done, You got one point!")
    score = score + 1
else:
    print("Sorry, Incorrect answer")

qn3 = input("What is DML commands? ")
if qn3.lower().strip() == "data manipulation language":
    print("Well done, You got one point!")
    score = score + 1
else:
    print("Sorry, Incorrect answer")

qn4 = input("Which type of network topology has one hub? ")
if qn4.lower().strip() == "star":
    print("Well done, You got one point!")
    score = score + 1
else:
    print("Sorry, Incorrect answer")

qn5 = input("What is the full form of SQL? ")
if qn5.lower().strip() == "structured query language":
    print("Well done, You got one point!")
    score = score + 1
else:
    print("Sorry, Incorrect answer")

print("You got "+str(score)+" questions correct")
print("You scored "+str((score/5)*100)+" %")
