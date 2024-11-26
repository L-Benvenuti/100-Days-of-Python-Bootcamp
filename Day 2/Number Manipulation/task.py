bmi = 84 / 1.65 ** 2
print(int(bmi)) # rounds to the lowest whole number - flooring
print(round(bmi)) # rounds to the nearest whole number
# OR it allows to round to a specific amount of decimal numbers

print(f"My BMI is {round(bmi)}")

score = 0
# User scores a point
score += 1
print(score)
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, and you are winning is {is_winning}")