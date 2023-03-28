from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
# title =  None
# word = None
current_card = {}

try:
    data = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(bgrnd, image=canvas_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(bgrnd, image=canvas_back_image)


def is_right():
    data_dict.remove(current_card)
    to_enter = pandas.DataFrame(data_dict)
    to_enter.to_csv("./data/word_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_back_image = PhotoImage(file="./images/card_back.png")
canvas_front_image = PhotoImage(file="./images/card_front.png")
bgrnd = canvas.create_image(400, 263, image=canvas_front_image)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_right)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
