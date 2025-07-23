import random

# Generate a list of 50 random floating-point numbers between 0 and 100
student_marks = [random.uniform(0, 100) for _ in range(50)]

# Round each mark to two decimal places
# rounded_marks = [round(mark, 2) for mark in student_marks]

# Print the list of rounded marks
# print(rounded_marks)

marks_above_90_in_list = [x for x in student_marks if(x>=90)]
print(marks_above_90_in_list)