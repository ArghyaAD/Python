import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Quiz")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.Turtle(image)

# def click(x, y):
#     print(x, y)
# turtle.onscreenclick(click)

data = pandas.read_csv("50_states.csv")
states = data.state
score = 0

while score < 50:
    user_input = screen.textinput(title=f"U.S.States Quiz {score}/50", prompt="Enter State Name : ").title()
    if user_input == "Exit":
        break
    for state in states:
        if state == user_input:
            X = int(data[states == user_input].x)
            Y = int(data[states == user_input].y)
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(X, Y)
            turtle.write(f"{user_input}")
            score += 1
