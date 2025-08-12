"""Virtual Coffe Machine
with 3 flavors, offering a built-in resource report that tracks:
- Watter, Milk and Coffe levels
- Profit margins"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def insert_coins():
    """Multiplies the number of coins for their value and  get the total payment amount"""
    while True:
        try:
            print("Please insert coins.")
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            return total
        except ValueError:
            print("Please type a numeric character.")

def are_ingredients_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change:.2f} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_type, ingredients_needed):
    """Deduct the ingredients needed to make the coffe from the resources available."""
    for ingredient in ingredients_needed:
        resources[ingredient] -= ingredients_needed[ingredient]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")

machine_on = True
profit = 0
while machine_on:

    choice = input('\nWhat would you like? (espresso/latte/cappuccino): ').lower()

    if choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice == 'off':
        machine_on = False

    elif choice in ("espresso", "latte", "cappuccino", "report"):
        drink = MENU[choice]
        print(f"The cost for your {choice} is ${drink['cost']:.2f}") # will add 2 decimal places
        if are_ingredients_sufficient(drink["ingredients"]):
            payment = insert_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid option.")


