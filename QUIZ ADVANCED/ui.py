from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.window.title("QUIZ GAME")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 125, text="lets try !!", fill=THEME_COLOR, width=280,
                                            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # score_label
        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        # buttons
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(bg=THEME_COLOR, image=self.true_image, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)
        self.false_button = Button(bg=THEME_COLOR, image=self.false_image, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.call_next_question()

        self.window.mainloop()

    def call_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text,text="QUIZ END!!")
        # self.window.after(2000, self.call_next_question)

    def true_pressed(self):
        check = self.quiz.check_answer("true")
        if check:
            self.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score : {self.score}/{self.quiz.question_number}")
        else:
            self.canvas.config(bg="red")
            self.score_label.config(text=f"Score : {self.score}/{self.quiz.question_number}")
        self.window.after(2000, self.call_next_question)

    def false_pressed(self):
        check = self.quiz.check_answer("false")
        if check:
            self.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score : {self.score}/{self.quiz.question_number}")
        else:
            self.canvas.config(bg="red")
            self.score_label.config(text=f"Score : {self.score}/{self.quiz.question_number}")
        self.window.after(2000, self.call_next_question)
