"""Virtual Coffee Machine | OPP Object-Oriented Programming"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine  = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f'\nWhat would you like? ({options}): ').lower()

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()

    elif choice == 'off':
        machine_on = False

    elif choice not in options or choice == "/":
        print("Invalid option.")

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
