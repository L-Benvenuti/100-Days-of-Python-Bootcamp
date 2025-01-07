def greet(name, place, wish):
    print(f"Hello {name}")
    print(f"Welcome to {place}")
    print(f"Hope you {wish}")

greet("Luiza", "Lui's town", "have a blast")

user_name = input("What's your name? ")
user_place = input("Tell me a place: ")
user_wish = input("What you wish yourself in this place? ")

greet(user_name, user_place, user_wish)

greet(input("name: "), input("place: "), input("wish: "))