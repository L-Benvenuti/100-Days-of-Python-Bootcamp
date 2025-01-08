# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art

print(art.logo)
print("Welcome to the secret auction program.")

isOver = False
auction = {}

while not isOver:
    user_name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction[user_name] = bid
    add_another_bidder = input("Would you like to add another bidder? 'Y' or 'N' ").lower()

    if add_another_bidder == "y":
        print("\n"*20)
    elif add_another_bidder == "n":
        isOver = True
        print("\n" * 20)

        highest_value = 0
        winner = ""
        for key in auction:
            if auction[key] > highest_value:
                highest_value = auction[key]
                winner = key

        print(f"The winner is {winner} with a bid of ${highest_value}")