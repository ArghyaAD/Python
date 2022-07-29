from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="TIMER")
    label_tick.config(text="")
    canvas.itemconfig(timer_text, text= "00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        label_timer.config(text="BREAK", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        label_timer.config(text="BREAK", fg=PINK)
        count_down(short_break)
    else:
        label_timer.config(text="TIMER", fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    global reps
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            ticks = ""
            for tick in range(int(reps / 2)):
                ticks += "✔"
            label_tick.config(text=ticks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("POMODORO")
window.minsize(width=400, height=400)
window.config(padx=50, pady=80, bg=YELLOW)

# canvas
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_image)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

# labels
label_timer = Label(text="TIMER", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_tick = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
label_tick.grid(column=1, row=4)

# buttons
start = Button(text="start", width=10, command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="reset", width=10, command=reset_timer)
reset.grid(column=2, row=3)

window.mainloop()
