print("WELCOME TO MY COMPUTER QUIZ !!")
print("NB: make sure that you don't have space at the end of your answers!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play ☺☻")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does CHEDOMI stand for? ")
if answer.lower() == "chezem dongmeza miguel":
    print("correct!")
    score += 1
else:
    print("incorrect!")

x = 6
c=str(x - score)
print("you got " + str(score) + " questions correct! " + "and " + c + " wrong questions on " + str(x) + " questions")
print("you got " + str((score / x)*100) + "%.")

