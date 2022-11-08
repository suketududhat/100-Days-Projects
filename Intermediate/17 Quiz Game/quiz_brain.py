class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        user_input = input(f"Q.{self.question_number} {question} True or False?: ")
