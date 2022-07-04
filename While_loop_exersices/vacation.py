money_needed = float(input())
money_at_the_moment = float(input())
days = 0
spend = 0
can_save = True
while money_at_the_moment < money_needed:
    command = input()
    current_input_of_money = float(input())
    if command == 'spend':
        spend += 1
        days += 1
        money_at_the_moment -= current_input_of_money
        if spend == 5:
            can_save = False
            break
        if money_at_the_moment < 0:
            money_at_the_moment = 0
    elif command == 'save':
        spend = 0
        days += 1
        money_at_the_moment += current_input_of_money


if can_save:
    print(f"You saved the money for {days} days.")
else:
    print("You can't save the money.")
    print(days)



