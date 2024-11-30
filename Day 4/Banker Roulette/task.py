import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option1
random_index = random.randint(0, 4)
print(friends[random_index])

#Option 2
print(random.choice(friends))