from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

# print(question_bank[0].text)
quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have answered all questions.")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")
