data = input()
mines = dict()

while data != "stop":
    number = int(input())
    if data not in mines:
        mines[data] = 0
    mines[data] += int(number)

    data = input()


for name, num in mines.items():
    print(f"{name} -> {num}")
