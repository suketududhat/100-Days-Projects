from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzie")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="test",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="EW", pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        # self.score_label.config(padx=20, pady=20)
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="Intermediate+/34 Quiz App/images/true.png")
        self.true_button = Button(
            image=true_img, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="Intermediate+/34 Quiz App/images/false.png")
        self.false_button = Button(
            image=false_img, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You have answered all questions!\n\nYour final score: {self.quiz.score}/{self.quiz.question_number}",
            )
            self.score_label.config(fg=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")
