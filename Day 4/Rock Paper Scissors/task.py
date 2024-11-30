import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice == 0:
    print("Rock" + rock)
elif player_choice == 1:
    print("Paper" + paper)
elif player_choice == 2:
    print("Scissors" + scissors)

computer_choice = random.randint(0, 2)
print("\nComputer chooses: ")
if computer_choice == 0:
    print("Rock" + rock)
elif computer_choice == 1:
    print("Paper" + paper)
elif computer_choice == 2:
    print("Scissors" + scissors)

if (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
    print("You lose")
elif player_choice == computer_choice:
    print("It's a tie")
else:
    print("You win!")

