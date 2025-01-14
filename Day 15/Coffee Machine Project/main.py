from data import MENU, resources
from functions import report, check_resources, check_money, make_coffee

def print_coins():
    quarters = int(input("How many quarters ($.25)?  "))
    dimes = int(input("How many dimes ($.10)?  "))
    nickles = int(input("How many nickles ($.05)?  "))
    pennies = int(input("How many pennies ($.01)?  "))

    return {"quarters": quarters, "dimes": dimes, "nickles": nickles, "pennies": pennies}

user_input = input("What would you like? (espresso/latte/cappuccino)\n").lower()

while not user_input == "off":
    if user_input == "report":
        report()
    elif user_input in MENU:
        if not check_resources(user_input):
            print(f"The price of {user_input} is ${MENU[user_input]["cost"]}.\nPlease insert coins.")
            able_to_pay = check_money(user_input, print_coins())

            if able_to_pay:
                make_coffee(user_input)

    user_input = input("\nWhat would you like? (espresso/latte/cappuccino)\n").lower()

