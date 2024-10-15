"""Love Calculator
You are going to write a function called calculate_love_score() 
that tests the compatibility between two names.  To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2-digit number and print it out.
e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 
Love Score = 53"""

def calculate_love_score(name1, name2):
    names = name1.upper() + name2.upper()
    names = {char: names.count(char) for char in set(names)} # Counting each letter in names

    true_total_sum = 0
    for key in "TRUE":
        if key in names:
            print(f"{key} occurs: {names[key]} times")
            true_total_sum += names[key]
        else: print(f"{key} occurs: 0 times")
    print(f"Total = {true_total_sum}")

    love_total_sum = 0
    for key in "LOVE":
        if key in names:
            print(f"{key} occurs: {names[key]} times")
            love_total_sum += names[key]
        else:
            print(f"{key} occurs: 0 times")
    print(f"Total = {love_total_sum}")

    print(f"Love Score = {true_total_sum}{love_total_sum}\n")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
