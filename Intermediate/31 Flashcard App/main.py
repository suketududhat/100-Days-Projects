from tkinter import *
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- CSV SETUP ------------------------------- #
try:
    df = pd.read_csv("Intermediate/31 Flashcard App/data/words_to_learn.csv")
except:
    df = pd.read_csv("Intermediate/31 Flashcard App/data/french_words.csv")
    df.to_csv("Intermediate/31 Flashcard App/data/words_to_learn.csv", index=False)
    df = pd.read_csv("Intermediate/31 Flashcard App/data/words_to_learn.csv")

word_list = df.to_dict(orient="records")
word_dict = {}

# ---------------------------- Functions ------------------------------- #
def learned_word():
    word_list.remove(word_dict)
    words_left = pd.DataFrame(word_list)
    words_left.to_csv(
        "Intermediate/31 Flashcard App/data/words_to_learn.csv", index=False
    )
    change_word()


def change_word():
    canvas.itemconfig(canvas_image, image=card_front_img)
    global word_dict, flip_timer
    window.after_cancel(flip_timer)
    word_dict = r.choice(word_list)
    french_word = word_dict["French"]
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=french_word, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    english_word = word_dict["English"]
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=english_word, fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas image
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="Intermediate/31 Flashcard App/images/card_front.png")
card_back_img = PhotoImage(file="Intermediate/31 Flashcard App/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas_title = canvas.create_text(
    400, 150, text="title", fill="black", font=("Ariel", 40, "italic")
)
canvas_word = canvas.create_text(
    400, 263, text="word", fill="black", font=("Ariel", 60, "bold")
)
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# Buttons
wrong_img = PhotoImage(file="Intermediate/31 Flashcard App/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(column=0, row=1)
right_img = PhotoImage(file="Intermediate/31 Flashcard App/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=learned_word)
right_button.grid(column=1, row=1)

change_word()
window.mainloop()
