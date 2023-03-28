from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
title =  None
word = None
def wrong_def():

    global data_dict, title, word
    ind = random.randint(0,100)
    canvas.itemconfig(title,text="")
    canvas.itemconfig(word,text="")
    title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    word = canvas.create_text(400, 263, text=data_dict['French'][ind], font=("Ariel", 60, "bold"))

def right_def():
    global data_dict, title, word
    ind = random.randint(0,100)
    canvas.itemconfig(title,text="")
    canvas.itemconfig(word,text="")
    title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    word = canvas.create_text(400, 263, text=data_dict['French'][ind], font=("Ariel", 60, "bold"))


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_back_image = PhotoImage(file="./images/card_back.png")
canvas_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=canvas_front_image)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong_def)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=right_def)
right_button.grid(column=1, row=1)

data =pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict()


window.mainloop()
