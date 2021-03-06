from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = list(map(chr, range(ord('a'), ord('z') + 1))) + list(map(chr, range(ord('A'), ord('Z') + 1)))
    numbers = list(map(str, range(10)))
    symbols = ['!', '#', '%', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)

    password_input.insert(0, password)

    window.update()

    messagebox.showinfo(title="Copied to clipboard!", message="The generated password was copied to the clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fiels empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        try:
            with open(file="data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating data
            data.update(new_data)

            with open(file="data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Website not found.")
        return

    try:
        website = website_input.get()
        json_data = data[website]
    except KeyError:
        messagebox.showwarning(title="Warning", message="Website not found.")
    else:
        # print(json_data['email'])
        email = json_data['email']
        password = json_data['password']

        messagebox.showinfo(title=website, message=f'The password was copied to the clipboard.\n\nWebsite: {website} \nEmail: {email} \nPassword: {password}')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'sys.ryan0902@gmail.com')

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)






window.mainloop()
