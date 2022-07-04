width = int(input())
lenght = int(input())
height = int(input())
total_space = width * lenght * height
there_is_space_left = True
command = input()
while command != 'Done':
    number_of_boxes = int(command)
    total_space -= number_of_boxes
    if total_space < 0:
        there_is_space_left = False
        break
    command = input()
if there_is_space_left:
    print(f"{total_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")