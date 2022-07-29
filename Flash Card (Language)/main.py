from tkinter import *
import pandas
import random


def change(a=1):
    with open("./data/french_words.csv") as data:
        file_content = pandas.read_csv(data)
        dict = file_content.to_dict(orient="records")
        random_word = random.choice(dict)
        french = random_word["French"]
        english = random_word["English"]
        if a % 2 != 0:
            canvas.itemconfig(canvas_image, image=front_end)
            canvas.itemconfig(lang, text="French")
            canvas.itemconfig(word, text=french)
        else:
            canvas.itemconfig(canvas_image, image=back_end)
            canvas.itemconfig(lang, text="English")
            canvas.itemconfig(word, text=english)
        canvas.after(5000, change, a + 1)


right_score = 0


def score_increase():
    global right_score
    right_score += 1
    canvas.itemconfig(right, text=f"Score : {right_score}")


wrong_score = 0


def score_decrease():
    global wrong_score
    wrong_score -= 1
    canvas.itemconfig(wrong, text=f"Score : {wrong_score}")


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

back_end = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_end = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_end)
lang = canvas.create_text(400, 120, text="LANG", font=("Arial", 40, "bold"))
word = canvas.create_text(400, 300, text="WORD", font=("Arial", 60, "bold"))
wrong = canvas.create_text(100, 100, text="Score : 0", font=("Arial", 25, "bold"))
right = canvas.create_text(670, 100, text="Score : 0", font=("Arial", 25, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_image, command=score_increase)
button_right.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_image, command=score_decrease)
button_wrong.grid(row=1, column=0)

change()

window.mainloop()
