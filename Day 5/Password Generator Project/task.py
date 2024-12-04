import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy
def select_random_elements(num_of_elements, arr):
    # randomly selects multiple elements and allows for repeated elements from sample
    return random.choices(arr, k=num_of_elements)  # returns array

pwd_letters = select_random_elements(nr_letters, letters)
pwd_symbols = select_random_elements(nr_symbols, symbols)
pwd_numbers = select_random_elements(nr_numbers, numbers)

password = "".join(pwd_letters) + "".join(pwd_symbols) + "".join(pwd_numbers) # transforms array into str
print(f"Easy password: {password}")

# Hard
# random.sample works the same way as random.choices but do not allow for repeated elements
password = "".join(random.sample(password, k=len(password)))
print(f"Hard password: {password}")

# OR
hard_password = pwd_letters + pwd_symbols + pwd_numbers
random.shuffle(hard_password)
print(f'Another hard password is: {"".join(hard_password)}')