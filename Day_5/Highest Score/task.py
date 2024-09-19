student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# Sum Scores with "sum" built-in function
print(sum(student_scores))
# Sum Scores with loop
sum = 0
for score in student_scores:
    sum += score
print(sum)

# Max Score with "max" built-in function
print(max(student_scores))
# Max Score with loop
max_score = None
for score in student_scores:
    if max_score is None or score > max_score: max_score = score
print(max_score)

# Min Score with "min" built-in function
print(min(student_scores))
# Max Score with loop
min_score = None
for score in student_scores:
    if min_score is None or score < min_score: min_score = score
print(min_score)

