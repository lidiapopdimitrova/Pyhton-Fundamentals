name_of_the_actor = input()
total_points = float(input())
number = int(input())

for i in range(number):
    name_of_jury = input()
    points_from_jury = float(input())
    total_points += len(name_of_jury) * points_from_jury / 2
    if total_points >= 1250.5:
        break
diff = abs(total_points - 1250.5)
if total_points >= 1250.5:
    print(f"Congratulations, {name_of_the_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_of_the_actor} you need {diff:.1f} more!")

