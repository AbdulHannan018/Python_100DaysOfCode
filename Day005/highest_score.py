exam_scores = [70, 80, 99, 84, 67, 88, 29, 58, 29, 89, 93, 81, 18]
print(sum(exam_scores))
print(max(exam_scores))

sum_scores = 0
for score in exam_scores:
    sum_scores += score
print("The total sum of exam scores is:", sum_scores)

highest_score = 0
for score in exam_scores:
    if score > highest_score:
        highest_score = score
print("The highest score is:", highest_score)