import random
rand_num = random.randint(1, 10) #Random integer, a <= N <=b
rand_num_0_to_1 = random.random() #Random floating number, 0.0 <= N < 1.0
# -- if random.random() * 5, random number between 0.0 and 5.0 (not included)
random_float = random.uniform(1, 10) #another way to generate floating point numbers

import my_module
print(my_module.my_favorite_number)

random_number = random.randint(1, 2)
if random_number == 1:
    print("Heads")
else:
    print("Tails")