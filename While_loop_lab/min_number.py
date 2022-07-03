import sys
min = sys.maxsize
while True:
    number = input()
    if number == 'Stop':
        break
    elif int(number) < min:
        min = int(number)


print(min)
