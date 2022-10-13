name = input("Type your name: ")
print("welcome", name, "to this adventure")

answer = input(
    "you are on a dirt road, it has come to an end and you can go left or right. which way would you like? ")

if answer == "left":
    answer = input("you come to the river, you can walk around it or swim across! type to walk around and swim to ")
    if answer == "swim":
        print("You swam across and were eaton by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of the water and lose the game")
    else:
        print("Not a valid option. You lose!")
elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross?")

    if answer == "back":
        print()
    elif answer == "cross":
        print()
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. you lose.")