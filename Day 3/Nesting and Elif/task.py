print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 12 or age >= 65 :
        print("Your ticket is $5, please.")
    elif age <= 18:
        print("Your ticket is $7, please.")
    else:
        print("Your ticket is $12, please.")
else:
    print("Sorry you have to grow taller before you can ride.")
