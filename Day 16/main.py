from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_input = input(f"What would you like? ({menu.get_items()})\n").lower()

while not user_input == "off":
    menu_options = ["espresso", "latte", "cappuccino"]
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input in menu_options:
        chosen_drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)

    user_input = input(f"\nWhat would you like? ({menu.get_items()})\n").lower()