from tkinter import *


def button_clicked():
    input_text = input.get()
    my_label["text"] = input_text


window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="new btn")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()

