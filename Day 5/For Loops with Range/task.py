# for number in range(1, 11): #does not include b digit (a,b)
#     print(number)
#
# for number in range(1, 11, 3): #stepping by 3
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(f"The answer to the Gauss Challenge is: {total}")