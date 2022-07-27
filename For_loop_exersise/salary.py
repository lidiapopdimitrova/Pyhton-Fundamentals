number_opened_tabs = int(input())
salary = int(input())
lost = 0
for i in range(number_opened_tabs):
    tab = input()
    if tab == "Facebook":
        lost += 150
    elif tab == "Reddit":
        lost += 50
    elif tab == "Instagram":
        lost += 100

    if salary <= lost:
        break
diff = abs(salary - lost)
if salary <= lost:
    print("You have lost your salary.")
else:
    print(diff)
