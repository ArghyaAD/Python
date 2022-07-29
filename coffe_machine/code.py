from menu import resources, MENU

order = input("What would you like? (espresso/latte/cappuccino):")


def calculate_amount():
    t_quarter = float(input("how many quarters?:"))
    t_dime = float(input("how many dimes?:"))
    t_nickel = float(input("how many nickels?:"))
    t_penny = float(input("how many pennies?:"))
    total_amount = (t_quarter * 0.25) + (t_dime * 0.10) + (t_nickel * 0.05) + (t_penny * 0.01)
    refund = total_amount - float(MENU[order]["cost"])
    return refund


do_prepare = True

while do_prepare:
    print("please enter your coins")
    total = calculate_amount()

    if total > 0:
        print(f"enjoy your {order}, and here is your exchange ${total}")
    if total < 0:
        print("not sufficient amount !!")
    for item in resources:
        resources[item] -= MENU[order]["ingredients"][item]
    order = input("What would you like? (espresso/latte/cappuccino):")
    for item2 in resources:
        if resources[item2] < MENU[order]["ingredients"][item2]:
            print("insufficient resources!")
            do_prepare = False
