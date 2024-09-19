''' The Gauss Challenge:
Gauss recognized he had fifty pairs of numbers
when he added the first and last number in the series,
the second and second-last number in the series, and so on.
For example: (1 + 100), (2 + 99), (3 + 98), etc
and each pair has a sum of 101.
50 pairs × 101 (the sum of each pair) = 5,050.'''

# Range Function
for number in range (1,11):
    print(number) # This prints each number starting by 1 and ends at 10

total_number = 1
for number in range (2,101):
    total_number += number # This line adds the current number to total_number. Ej 0+1=1, then 1+2=3, etc
print(total_number)

'''FizzBuzz Game
Rules:
- Print each number from 1 to 100 in turn and include number 100.
- When the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- If the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0: print("FizzBuzz")
    elif number % 3 == 0: print("Fizz")
    elif number % 5 == 0: print("Buzz")
    else: print(number)
    

