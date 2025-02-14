while True:
    try:
        age = int(input("How old are you? "))
        if age > 18:
            print(f"You can drive at age {age}.")
            break
        else:
            print(f"You are not allowed to drive at age {age}.")
            break
    except ValueError:
        print("Invalid option. Please type a number.")

