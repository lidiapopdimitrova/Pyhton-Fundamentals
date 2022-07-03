import sys
max = -sys.maxsize
while True:
    number = input()
    if number == 'Stop':
        break
    elif int(number) > max:
        max = int(number)


print(max)

