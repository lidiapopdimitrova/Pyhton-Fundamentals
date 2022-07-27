number_of_groups = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
for i in range(number_of_groups):
    people_in_the_group = int(input())
    if people_in_the_group <= 5:
        g1 += people_in_the_group
    elif people_in_the_group <= 12:
        g2 += people_in_the_group
    elif people_in_the_group <= 25:
        g3 += people_in_the_group
    elif people_in_the_group <= 40:
        g4 += people_in_the_group
    else:
        g5 += people_in_the_group

total_people = g1 + g2 + g3 + g4 + g5
g1p = g1 / total_people * 100
g2p = g2 / total_people * 100
g3p = g3 / total_people * 100
g4p = g4 / total_people * 100
g5p = g5 / total_people * 100
print(f"{g1p:.2f}%")
print(f"{g2p:.2f}%")
print(f"{g3p:.2f}%")
print(f"{g4p:.2f}%")
print(f"{g5p:.2f}%")
