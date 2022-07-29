# from turtle import Turtle, Screen, Shape
#
# nemo = Turtle()
# nemo.color("yellow")
# nemo.fd(100)
# my_screen = Screen()
# nemo.shape("turtle")
# my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["pikachu","raichu","kochu"])
table.add_column("Type",["electric","water","fire"])
table.align="l"
print(table)

