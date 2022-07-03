name = input()
average = 0
grade_num = 0
fail = 0
while True:
    grade = float(input())
    grade_num += 1
    if grade >= 4:
        average += grade
        average_grade = average / grade_num
        if grade_num >= 12:
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
            break

    elif grade < 4:
        fail += 1
        if fail == 2:
            print(f"{name} has been excluded at {grade_num - 1} grade")
            break

# student = input()
#
# student_class = 1
# total_grade = 0
# bad_grade = 0
#
# while student_class <= 12 and bad_grade != 2:
#     current_grade = float(input())
#     if current_grade >= 4:
#         total_grade += current_grade
#         student_class += 1
#     else:
#         bad_grade += 1
#
# if bad_grade == 2:
#     print(f"{student} has been excluded at {student_class} grade")
# else:
#     avg_grade = total_grade / 12
#     print(f"{student} graduated. Average grade: {avg_grade:.2f}")