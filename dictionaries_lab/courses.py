data = input()
courses = dict()

while data != "end":
    course, student = data.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    data = input()

for course, names in courses.items():
    print(f"{course}: {len(names)}")
    for person in courses[course]:
        print(f"-- {person}")
