from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# pictures
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png").resize((100, 100)))
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png").resize((100, 100)))
rock_img_com = ImageTk.PhotoImage(Image.open("rock1.png").resize((100, 100)))
scissor_img_com = ImageTk.PhotoImage(Image.open("scissor1.png").resize((100, 100)))
paper_img_com = ImageTk.PhotoImage(Image.open("paper1.png").resize((100, 100)))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=rock_img_com, bg="#9b59b6")
user_label.grid(row=1, column=0)
comp_label.grid(row=1, column=6)


# scores
playerscore = Label(root, text="0", font=("arial", 14), bg="#9b59b6", fg="white")
computerscore = Label(root, text="0", font=("arial", 14), bg="#9b59b6", fg="white")
playerscore.grid(row=1, column=2)
computerscore.grid(row=1, column=4)

# indicators
user_indicator = Label(root, font=("algerian", 10), text="User", bg="#9b59b6", fg="white")
computer_indicator = Label(root, font=("algerian", 10), text="Computer", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=0)
computer_indicator.grid(row=0, column=6)


# messages
msg = Label(root, text="it's tie", font=("calibri", 16))
msg.grid(row=1, column=3)


# update messages
def updateMessage(x):
    msg['text'] = x


# update user score
def updateUserScore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)


# update computer score
def updateComScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)


# check winner
def checkwin(player, computer):
    if player == computer:
        updateMessage("its a tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("computer wins")
            updateComScore()
        else:
            updateMessage("you wins")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("computer wins")
            updateComScore()
        else:
            updateMessage("you wins")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("computer wins")
            updateComScore()
        else:
            updateMessage("you wins")
            updateUserScore()
    else:
        pass


# update choices
choices = ["rock", "scissor", "paper"]
def updatechoice(x):

# for computer
    CompChoice = choices[randint(0, 2)]
    if CompChoice == "rock":
        comp_label.configure(image=rock_img_com)
    elif CompChoice == "scissor":
        comp_label.configure(image=scissor_img_com)
    else:
        comp_label.configure(image=paper_img_com)

# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "scissor":
        user_label.configure(image=scissor_img)
    else:
        user_label.configure(image=paper_img)
    checkwin(x, CompChoice)


# buttons
rock = Button(root, font=("algerian", 10), command=lambda: updatechoice("rock"), width=20, height=2, text="Rock", bg="#FF3E4D", fg="black")
scissor = Button(root, font=("algerian", 10), command=lambda: updatechoice("scissor"), width=20, height=2, text="Scissor", bg="#Fad02e", fg="black")
paper = Button(root, font=("algerian", 10), command=lambda: updatechoice("paper"), width=20, height=2, text="paper", bg="#0ABDE3", fg="black")
rock.grid(row=2, column=2)
scissor.grid(row=2, column=3)
paper.grid(row=2, column=4)


def quit1():
    root.destroy()


b1 = Button(root, text="x", command=quit1, font=("algerian", 10), bg="yellow", fg="black")
b1.grid(row=10, column=0)

c1 = Label(root, font=("algerian", 14, "bold"), text="by CHEDOMI", bg="orange", fg="blue").grid(row=10, column=6)


root.mainloop()
