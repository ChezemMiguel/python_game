from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Game Rock paper and scissor")
window.configure(background="black")

# open the different images
image_rock2 = ImageTk.PhotoImage(Image.open("rock-user.png").resize((100, 100)))
image_paper2 = ImageTk.PhotoImage(Image.open("paper-user.png").resize((100, 100)))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor-user.png").resize((100, 100)))
image_rock1 = ImageTk.PhotoImage(Image.open("rock1.png").resize((100, 100)))
image_paper1 = ImageTk.PhotoImage(Image.open("paper1.png").resize((100, 100)))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png").resize((100, 100)))

# create images as labels
label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# create scores labels
computer_score = Label(window, text=0, font=("arial", 60, "bold"), bg="orange", fg="black")
player_score = Label(window, text=0, font=("arial", 60, "bold"), bg="orange", fg="black")
computer_score.grid(row=1, column=3)
player_score.grid(row=1, column=1)

player_indicator = Label(window, font=("algerian", 20, "bold"),
                         text="COMPUTER", bg="orange", fg="blue")

computer_indicator = Label(window, font=("algerian", 20, "bold"),
                           text="PLAYER", bg="orange", fg="blue")

computer_indicator.grid(row=0, column=4)
player_indicator.grid(row=0, column=0)

# creation of different functions.


def update_message(a):
    final_message['text'] = a


def computer_update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)


def player_update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)


def winner_check(p, c):
    if p == c:
        update_message("       it's a tie!!       ")
    elif p == "rock":
        if c == "paper":
            update_message("Computer Wins!!")
            computer_update()
        else:
            update_message("   Player Wins!!   ")
            player_update()
    elif p == "paper":
        if c == "scissor":
            update_message("Computer wins!!")
            player_update()
        else:
            update_message("   Player Wins!!   ")
            computer_update()
    elif p == "scissor":
        if c == "rock":
            update_message("Computer Wins!!")
            player_update()
        else:
            update_message("   Player Wins!!   ")
            computer_update()
    else:
        pass


to_select = ["rock", "paper", "scissor"]


def choice_update(a):

    choice_computer = to_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    if a == "rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)
    winner_check(a, choice_computer)


final_message = Label(window, text="it's a tie", font=("arial", 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)

# creation of the different buttons(choices)
button_rock = Button(window, width=20, height=2, text="ROCK",
                     font=("arial", 14, "bold"), bg="yellow", fg="red", command=lambda: choice_update("rock")).grid(row=2, column=1)

button_paper = Button(window, width=20, height=2, text="PAPER",
                      font=("arial", 14, "bold"), bg="yellow", fg="red", command=lambda: choice_update("paper")).grid(row=2, column=2)

button_scissor = Button(window, width=20, height=2, text="SCISSOR",
                        font=("arial", 14, "bold"), bg="yellow", fg="red", command=lambda: choice_update("scissor")).grid(row=2, column=3)

c1 = Label(window, font=("algerian", 14, "bold"), text="by CHEDOMI", bg="orange", fg="blue").grid(row=10, column=4)


window.resizable(0, 0)
window.mainloop()