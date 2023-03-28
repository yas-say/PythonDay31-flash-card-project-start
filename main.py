from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



window = Tk()
window.title("Flash cards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(height=300, width=500, bg="white", highlightthickness=0)
canvas_back_image = PhotoImage(file="./images/card_back.png")
canvas_front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(250,150, image=canvas_back_image)
canvas.grid(column=0,row=0, columnspan=2)


right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1,row=1)


wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0,row=1)

window.mainloop()