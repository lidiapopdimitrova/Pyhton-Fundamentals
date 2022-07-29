import sys
number = int(input())
minimum = sys.maxsize
maximum = -sys.maxsize - 1

for i in range(0, number):
    current_number = int(input())
    if current_number > maximum:
        maximum = current_number

    if current_number < minimum:
        minimum = current_number


print(f"Max number: {maximum}")
print(f"Min number: {minimum}")
