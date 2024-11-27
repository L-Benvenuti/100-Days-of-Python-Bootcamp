print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
can_go_in = False

if height >= 120:
    can_go_in = True
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill += 5
    elif age <= 18:
        print("Please pay $7.")
        bill += 7
    else:
        print("Please pay $12.")
        bill += 12
else:
    print("Sorry you have to grow taller before you can ride.")

if can_go_in:
    right_answer = False
    while not right_answer:
        wants_popcorn = input("Would you like some popcorn to take with you? ").lower()
        if wants_popcorn == "yes" or wants_popcorn == "y":
            print("Awesome! That will be an extra $3, please.")
            bill += 3
            right_answer = True
        elif wants_popcorn == "no" or wants_popcorn == "n":
            print("Well... You're the one missing out.")
            right_answer = True
        else:
            print("That doesn't really answer my question, does it?! Let's try that again...")

    print(f"Okay, so your total is ${bill}")