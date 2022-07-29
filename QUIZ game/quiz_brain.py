class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_input = input(f"Q{self.question_number}:{self.current_question.text} (True/False):")

    def still_has_questions(self):
        if self.question_number == 12:
            return False
        else:
            return True

    def check_answer(self):
        if self.user_input.lower() == self.current_question.answer.lower():
            print("Right Answer!!")
            self.score += 1
        else:
            print("Wrong Answer!!")
        print(f"correct answer is {self.current_question.answer}")
        print(f"Your score is {self.score}/{self.question_number}")
