# Functions with 1 input
def greet(name):
    print(f"Hey {name}")
    print(f"How do you do {name}?")
    print(f"Welcome {name}")
greet("Zulema")
greet("Iveth")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Whats is it like in {location}?")
greet_with("Zulema", "NJ")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Whats is it like in {location}?")
greet_with(location="Mexico", name="Iveth")

