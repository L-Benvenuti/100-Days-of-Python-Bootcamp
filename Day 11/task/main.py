import art
import random

# OTHER FUNCTIONS
def total_sum(array_to_sum):
    total = 0
    for number in array_to_sum:
        total += number
    return total

def check_for_ace(card, current_total):
    if card == 1:
        if current_total <= 10:
            return 11
        else:
            return 1
    else:
        return card

def computer_plays(cards, computer_array):
    computer_array.append(check_for_ace(random.choice(cards), total_sum(computer_array)))

    while (total_sum(computer_array) < 21) and not (total_sum(computer_array) > 16):
        computer_array.append(check_for_ace(random.choice(cards), total_sum(computer_array)))

    if total_sum(computer_array) > 21:
        return ["lose", computer_array]
    elif total_sum(computer_array) > 16:
        return ["proceed", computer_array]

def end_game(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose!"
    elif player_score == computer_score:
        return "Wow, that was close... It's a draw!"
    elif player_score > computer_score:
        return "You did it! You won!"
    elif player_score < computer_score:
        return "Unfortunately, the house always wins... You lose!"


# GAME - INITIALIZATION OF VARIABLES AND COMBINATION OF FUNCTIONS
def game():
    '''This function will help initialize all variables and the game logic in a single place'''
    # VARIABLES
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    computer = []

    # GAME STARTS
    # one card for the computer & computer main print statement
    computer.append(check_for_ace(random.choice(cards), 0))
    computer_first_statement = f"\tComputer's first card: {computer[0]}"

    # two cards for the player & player continuous print statement
    player.append(check_for_ace(random.choice(cards), 0)) #first card so total = 0
    player.append(check_for_ace(random.choice(cards), total_sum(player)))

    # STARTING PRINT STATEMENTS
    print(art.logo)
    print(f"\tYour cards: {player}, current score: {total_sum(player)}")
    print(computer_first_statement)


    # CARD HANDLING
    want_more_cards = True
    while want_more_cards:
        if total_sum(player) == 21:
            another_card = 'n'
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == 'y':
            # add another card to player
            player.append(check_for_ace(random.choice(cards), total_sum(player)))

            print(f"\tYour cards: {player}, current score: {total_sum(player)}")
            print(computer_first_statement)

            if total_sum(player) > 21:
                print(f"\tYour final hand: {player}, final score: {total_sum(player)}")
                print(f"\tComputer's final hand: {computer}, final score: {total_sum(computer)}")
                print(end_game(total_sum(player), total_sum(computer)))
                want_more_cards = False

        elif another_card == 'n':
            # player doesn't want more cards, therefore time for the computer to play
            computer_result = computer_plays(cards, computer)
            if computer_result[0] == "lose":
                print(f"\tYour final hand: {player}, final score: {total_sum(player)}")
                print(f"\tComputer's final hand: {computer_result[1]}, final score: {total_sum(computer_result[1])}")
                print("\tComputer went over. You won!")
            else:
                print(f"\tYour final hand: {player}, final score: {total_sum(player)}")
                print(f"\tComputer's final hand: {computer_result[1]}, final score: {total_sum(computer_result[1])}")
                print(end_game(total_sum(player), total_sum(computer_result[1])))
                want_more_cards = False



# CALLING GAME FUNCTION TO START THE GAME
want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if want_to_play == "y":
    game_over = False
    while not game_over:
        game()
        want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if not want_to_play == 'y':
            game_over = True
else:
    print("Oh well, that's unfortunate... Goodbye then")