number_of_commands = int(input())

users_currently = {}

for i in range(number_of_commands):
    data = input().split()
    if len(data) == 3:
        command, username, licence_plate_number = data
        if username not in users_currently:
            users_currently[username] = licence_plate_number
            print(f"{username} registered {licence_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {licence_plate_number}")

    elif len(data) == 2:
        command, username = data
        if username not in users_currently:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            users_currently.pop(username)

for name, number in users_currently.items():
    print(f"{name} => {number}")
