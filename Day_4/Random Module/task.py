import random
import my_module

random_integer = random.randint(1,10)
print(random_integer)

print(my_module.my_favourite_number)

random_numer_0_to_1 = random.random() * 10
print(random_numer_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

coin = random.randint(1,2)
if coin == 1:
    print("Heads")
else:
    print("Tails")

