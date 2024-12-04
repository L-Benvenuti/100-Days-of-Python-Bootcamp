student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# total_sum = 0
# for score in student_scores:
#     total_sum += score
# print(total_sum)

# student_scores
print(max(student_scores))

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print(max_value)