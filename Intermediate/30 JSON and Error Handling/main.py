from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {"username": username, "password": password}}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.askokcancel(
            title="Error", message="Please don't leave any fields blank!"
        )
    else:
        try:
            with open(
                "Intermediate/30 JSON and Error Handling/data.json", "r"
            ) as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(
                "Intermediate/30 JSON and Error Handling/data.json", "w"
            ) as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(
                "Intermediate/30 JSON and Error Handling/data.json", "w"
            ) as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(
            "Intermediate/30 JSON and Error Handling/data.json", "r"
        ) as data_file:
            data = json.load(data_file)
            data = data[website]
    except FileNotFoundError:
        messagebox.askokcancel(title="Error", message="No password stored yet.")
    except KeyError:
        messagebox.askokcancel(
            title="Error", message="No such website. Please try again."
        )
    else:
        username = data["username"]
        password = data["password"]
        messagebox.askokcancel(
            title=f"Search Result for {website}",
            message=f"Username - {username} \nPassword - {password}",
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="Intermediate/29 Password Manager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "exampleemail@awesome.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
generatepass_button = Button(text="Generate Password", command=generate_password)
generatepass_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
