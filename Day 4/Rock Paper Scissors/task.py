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

computer_random_choice = random.randint(0,2)
if computer_random_choice == 0:
    computer_choice_img = rock
    computer_choice = "rock"
elif computer_random_choice == 1:
    computer_choice_img = paper
    computer_choice = "paper"
else:
    computer_choice_img = scissors
    computer_choice = "scissors"

noChoice = True
user_choice = "none"

print("Welcome to rock, paper, scissors!")
print("Choose your pick...")
while noChoice:
    user_choice = input("Rock, Paper, or Scissors: \n").lower()
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        noChoice = False
    print("Come on man, you're the one that started the game, just choose a damn hand...")

if user_choice == "rock":
    user_choice_img = rock
elif user_choice == "paper":
    user_choice_img = paper
else:
    user_choice_img = scissors


if (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    result = "you win!"
elif (computer_choice == "rock" and user_choice == "scissors") or (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper"):
    result = "you lose!"
else:
    result = "it's a tie!"

print(f"You picked: \n{user_choice_img}{user_choice.upper()}\n")
print(f"Computer picked: \n{computer_choice_img}{computer_choice.upper()}\n")
print(f"Therefore, {result}")
