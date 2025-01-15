from data import question_data
from quiz_brain import QuizBrain
from question_bank_model import QuestionBank

print("Welcome to Crazy Quiz!")
print("These are our categories:")

number = 1
for option in question_data:
    print(f"{number}. {option["category"]}")
    number += 1

right_answer = False

while not right_answer:
    user_category_index = int(input("Which type of quiz do you fancy today? Type the number of the category.\n")) - 1
    print("\n")
    if user_category_index >= 0 and user_category_index < len(question_data):
        right_answer = True

data = question_data[user_category_index]["data"]
data_bank = QuestionBank(data)

chosen_list = data_bank.create_question_bank()
quiz = QuizBrain(chosen_list)

while quiz.still_has_questions():
    quiz.next_question()

quiz.end_game()