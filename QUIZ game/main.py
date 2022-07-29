from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    TEXT = item["text"]
    ANSWER = item["answer"]
    ques = Question(TEXT, ANSWER)
    question_bank.append(ques)

new_question = QuizBrain(question_bank)

# for i in question_data:
#     new_question.next_question()

while new_question.still_has_questions():
    new_question.next_question()
    new_question.check_answer()
