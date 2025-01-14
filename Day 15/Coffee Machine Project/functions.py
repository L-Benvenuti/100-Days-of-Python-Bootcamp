from data import MENU, resources

def report():
    for key in resources:
        if key == "water" or key == "milk":
            string = f"{resources[key]}ml"
        elif key == "coffee":
            string = f"{resources[key]}g"
        else:
            string = f"${resources[key]}"
        print(f"{key.capitalize()}: {string}")

def check_resources(drink):
    drink_ingredients = MENU[drink]["ingredients"]

    lack_resource = False

    if drink_ingredients["water"] > resources["water"]:
        print(f"Sorry not enough water")
        lack_resource = True
    if drink_ingredients["milk"] > resources["milk"]:
        print(f"Sorry not enough milk")
        lack_resource = True
    if drink_ingredients["coffee"] > resources["coffee"]:
        print(f"Sorry not enough coffee")
        lack_resource = True

    if lack_resource:
        return True

def check_money(drink, coins):
    drink_cost = MENU[drink]["cost"]
    total_payed = (coins["quarters"]*0.25) + (coins["dimes"]*0.10) + (coins["nickles"]*0.05) + (coins["pennies"]*0.01)

    if total_payed < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        if total_payed > drink_cost:
            change = total_payed - drink_cost
            print(f"Here is ${change}")

        resources["money"] += drink_cost
        return True

def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink} ☕️ Enjoy!")