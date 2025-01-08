import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
user_num1 = float(input("What's the first number?    "))

isOver = False

while not isOver:
    print("+\n-\n*\n/")
    operation = input("Pick an operation:    ")
    user_num2 = float(input("What's the second number?    "))

    if operation not in functions:
        print("Something might have gone wrong try again...\n\n")
        print(f"Your first number still is:    {user_num1}")
    else:
        total = functions[operation](user_num1, user_num2)
        print(f"{user_num1} {operation} {user_num2} = {total}")
        want_to_continue = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation:    ").lower()

        if want_to_continue == "y":
           user_num1 = total
        else:
            print(f"Your final total is: {total}")
            isOver = True