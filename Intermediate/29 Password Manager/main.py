from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(
    file="C:/Users/suk2d/pyproj/Udemy/100-Days-Projects/Intermediate/29 Password Manager/logo.png"
)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="W")
generatepass_button = Button(text="Generate Password")  # , command=action)
generatepass_button.grid(column=2, row=3)

add_button = Button(text="Add")  # , command=action)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
