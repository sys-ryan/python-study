from tkinter import *

import pandas
import pandas as pd
import random




# Functions
def get_data_from_file(filepath):
    data = pd.read_csv(filepath)
    data = data.to_dict(orient="records")
    return data

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="Español", fill="black")
    canvas.itemconfig(card_word, text=current_card["Word"], fill="black")
    canvas.itemconfig(card, image=card_font)

    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["Meaning"], fill="white")

def is_right():
    data.remove(current_card)
    print(len(data))
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Data
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = get_data_from_file('data/words_to_learn.csv')
except FileNotFoundError:
    data = get_data_from_file('data/filtered-data.csv')
current_card = {}






# Components
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)

card_font = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_font)
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))


wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_right)
right_button.grid(column=1, row=1)

next_card()


window.mainloop()

