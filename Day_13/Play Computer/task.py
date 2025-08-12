while True:

    try:
        year = int(input("What's your year of birth? "))
        if year < 1980:
            print("You are not a millennial or Gen Z.")
        elif year >= 1980 and year <= 1994:
            print("You are a millennial.")
        elif year >= 1995:
            print("You are a Gen Z.")

    except ValueError:
        print("Invalid option. Please type a number.")

