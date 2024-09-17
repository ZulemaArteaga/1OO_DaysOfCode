print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    # age 12- 17 pay $5
    if 12 <= age <= 17:
        bill = 5
        print("Child tickets are $5.")
    # age 18 to 44 pay $7
    if 18 <= age <= 44:
        bill = 7
        print("Youth tickets are $7.")
    # age 45 to 55 ride free
    if 45 <= age <= 55:
        bill = 0
    if age >= 56:
        bill = 12


    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

