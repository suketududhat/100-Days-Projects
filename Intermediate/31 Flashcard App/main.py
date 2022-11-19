from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas image
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="Intermediate/31 Flashcard App/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
language_text = canvas.create_text(
    400, 150, text="French", fill="black", font=("Ariel", 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# Buttons
wrong_img = PhotoImage(file="Intermediate/31 Flashcard App/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_img = PhotoImage(file="Intermediate/31 Flashcard App/images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
