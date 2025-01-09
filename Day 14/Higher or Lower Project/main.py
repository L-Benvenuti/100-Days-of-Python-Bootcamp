from art import vs, logo
from game_data import data
import random

def compare_followers(highest, lowest):
    if highest['follower_count'] > lowest['follower_count']:
        return {'result': True, 'most_followers': highest}
    else:
        return {'result': False, 'most_followers': lowest}

score = 0
game_over = False
item_a = random.choice(data)
print(logo)


while not game_over:
    item_b = random.choice(data)
    while item_b == item_a:
        '''makes sure the two items are not the same'''
        item_b = random.choice(data)


    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")
    user_guess = input("Who has more followers? Type 'A' or 'B':    ").lower()
    answers = ['a', 'b']

    while user_guess not in answers:
        user_guess = input("If you want to play the game, I'm going to ask again... Who has more followers? 'A' or 'B':    ").lower()

    if user_guess == "a":
        is_right = compare_followers(item_a, item_b)
    else:
        is_right = compare_followers(item_b, item_a)

    if is_right['result']:
        score += 1
        item_a = is_right['most_followers']
        print('\n' * 20)
        print(logo)
        print(f"You're right! Current score: {score}")

    else:
        game_over = True
        print('\n' * 20)
        print(logo)
        print(f"Sorry, that's wrong. The most followed is: {is_right['most_followers']['name']}, with {is_right['most_followers']['follower_count']} million followers.\nYour final score: {score}")