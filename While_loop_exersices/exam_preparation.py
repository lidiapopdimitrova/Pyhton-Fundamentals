max_bad_grades = int(input())
bad_grades_number = 0
average_grades = 0
number_of_problems = 0
is_expeled = False
last_problem = ''
problem = input()
while problem != 'Enough':
    grade = int(input())
    if grade <= 4:
        bad_grades_number += 1
        if bad_grades_number == max_bad_grades:
            is_expeled = True
            break
    average_grades += grade
    number_of_problems += 1
    last_problem = problem
    problem = input()


if is_expeled:
    print(f"You need a break, {bad_grades_number} poor grades.")
else:
    average_grades /= number_of_problems
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
