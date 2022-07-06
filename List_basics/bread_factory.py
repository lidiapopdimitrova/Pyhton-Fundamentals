work_events = input().split("|")
energy = 100
coins = 100
gained_energy = 0

for work in work_events:
    is_over = False
    worked = work.split("-")
    event = worked[0]
    number = int(worked[1])

    if event == 'rest':
        if (energy + number) <= 100:
            energy += number
            gained_energy = number
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            print('You had to rest!')
            energy += 50

    else:
        if coins >= number:
            print(f"You bought {event}.")
            coins -= number
        elif coins < number:
            print(f"Closed! Cannot afford {event}.")
            is_over = True
            break


if is_over == False:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")