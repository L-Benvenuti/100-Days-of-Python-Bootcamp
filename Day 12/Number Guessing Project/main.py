import art
import random

def check_number(user_guess, number):
    if user_guess == number:
        print("You did it! You guessed it right!")
        return "Done"
    elif user_guess > number:
        print("Too high.")
    else:
        print("Too low.")
    print("Guess again.")

print(art.logo)
print("Welcome to the Number Guessing Game!")

possible_input_answers = ['easy', 'hard', 'y', 'n']

is_done = False
computer_statement = "I'm thinking of a number between 1 and 100."

while not is_done:
    difficulty = input("Choose the difficulty. Type 'easy' or 'hard':    ")

    while difficulty not in possible_input_answers:
        difficulty = input("That's not what I asked... do you want it to be 'easy' or 'hard':    ")

    random_number = random.randint(1, 100)
    print(random_number)
    lives = 0

    if difficulty == 'easy':
        lives += 10
    elif difficulty == 'hard':
        lives += 5

    print(computer_statement)

    right_guess = False

    while not right_guess:
        print(f"You have {lives} attempts left to guess the number.")
        guess = int(input("Make a guess:    "))
        result = check_number(guess, random_number)
        if result:
            right_guess = True
        lives -= 1

    continue_playing = input("Do you want to continue playing? 'y' or 'n'?    ")

    while continue_playing not in possible_input_answers:
        continue_playing = input("Bruh, again? That's not what I asked... Do you want to continue playing? 'y' or 'n'?    ")

    if continue_playing == 'n':
        is_done = True
        print("Okay, bye...")
    else:
        print("Okay, let's play again!!!\n")