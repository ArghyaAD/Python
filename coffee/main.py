from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

to_make=True
menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
# cost={
#     "latte":2.5,
#     "espresso":1.5,
#     "cappuccino":3
# }

while to_make:
    order=input("what do you want?:")

    if order=="report":
        coffee_maker.report()
        money_machine.report()
    if order=="off":
        to_make=False

    drink = menu.find_drink(order)

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




