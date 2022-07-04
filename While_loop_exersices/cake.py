width = int(input())
lenght = int(input())
slices_of_cake = width * lenght
no_cake_left = False
command = input()
while command != 'STOP':
    number = int(command)
    slices_of_cake -= number
    if slices_of_cake < 0:
        no_cake_left = True
        break
    command = input()
if no_cake_left:
    print(f"No more cake left! You need {abs(slices_of_cake)} pieces more.")
else:
    print(f"{slices_of_cake} pieces are left.")