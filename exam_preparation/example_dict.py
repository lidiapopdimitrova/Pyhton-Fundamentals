n = int(input())
game_dict = {}
for _ in range(n):
    info = input().split('|')
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    game_dict[car] = [mileage, fuel]
command_data = input().split(' : ')
while command_data[0] != 'Stop':
    command = command_data[0]
    car = command_data[1]

    if command == "Drive":
        distance = int(command_data[2])
        fuel = int(command_data[3])
        if fuel > game_dict[car][1]:
            print("Not enough fuel to make that ride")
        else:
            game_dict[car][0] += distance
            game_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if game_dict[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del game_dict[car]
    elif command == 'Refuel':
        fuel = int(command_data[2])
        if game_dict[car][1] + fuel > 75:
            fuel = 75 - game_dict[car][1]
        game_dict[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        kilometers = int(command_data[2])
        if game_dict[car][0] - kilometers < 10000:
            game_dict[car][0] = 10000
        else:
            game_dict[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command_data = input().split(' : ')
for key, value in game_dict.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")