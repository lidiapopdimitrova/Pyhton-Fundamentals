number = int(input())
grades = dict()

for i in range(number):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

filtered_grades = {}
for student_name, list_grades in grades.items():
    average_grade = sum(list_grades) / len(list_grades)
    if average_grade >= 4.5:
        filtered_grades[student_name] = average_grade

# sorted_student_grades = sorted(filtered_grades.items(), key=lambda kvp: -kvp[1])

for st_name, avg in filtered_grades.items():
    print(f"{st_name} -> {avg:.2f}")

