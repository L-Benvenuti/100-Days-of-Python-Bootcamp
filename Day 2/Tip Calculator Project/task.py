print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

final_tip = bill * (tip / 100)
total_per_person = (bill + final_tip) / people
print(f"Each person should pay: ${total_per_person:.2f}")
# :.2f at the end formats the number to in this case 2 decimal places