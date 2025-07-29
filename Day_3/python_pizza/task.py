print("Welcome to Python Pizza Deliveries!")
# bill = 0
# size = input("What size pizza do you want? S, M or L: ")
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# elif size == "l":
#     bill += 25
#
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill += 3
# else:
#     pass
#
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")

bill = 0
size = input("What size pizza do you want? S, M, or L: ").lower()
bill += 15 if size == 's' else 20 if size == 'm' else 25 if size == 'l' else 0

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if pepperoni == 'y':
    bill += 2 if size == 's' else 3

extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if extra_cheese == 'y':
    bill += 1

print(f"Your final bill is: ${bill}.")