"""Prime Number Checker
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
--> https://en.wikipedia.org/wiki/Prime_number
You need to write a function called is_prime() that checks whether if the number passed into
it is a prime number or not.  It should return True or False.
e.g.
7 is a primer number because it is only divisible by 1 and itself.
But 4 is not a prime number because you can divide it by 1, 2 or 4.

NOTE: 2 is a prime number because it's only divisible by 1 and itself,
but 1 is not a prime number because it is only divisible by 1.
Example Input 1
73
Example Output 1
True
Example Input 2
75
Example Output 2
False"""

import  math

def is_prime(num):
    """This function checks if a number is prime
    A prime number is a positive integer greater than 1
    that has no positive divisors other than 1 and itself"""

    square_root = int(math.sqrt(num))
    # Getting the square root if "num"

    if num <= 1:
        #  If the number is less than or equal to 1, it's not a prime number
        return False

    for divisor in range(2, square_root + 1):
    # Loop to check if num is divisible by any integer from range 2 to the square root number
        if num % divisor == 0:
            return False
            # If divisible, it's not a prime number
    else:
        return True
        # If no divisors were found, num is prime

number = int(input("\nEnter a number to determine whether it is a prime number or not: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is NOT a prime number.")



