import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Print random friend. Option 1.
print(random.choice(friends))

# Print random friend. Option 2.
random_index = random.randint(0,4)
print((friends[random_index]))
