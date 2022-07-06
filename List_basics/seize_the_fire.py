fire_input = input().split("#")
water_amount = int(input())
condition = False
effort = 0
total_fire = 0
print('Cells:')

for fire in fire_input:
    fire_info = fire.split(" = ")
    type_of_fire = fire_info[0]
    cells = int(fire_info[1])
    condition = False

    if type_of_fire == 'High':
        if 81 <= cells <= 125:
            condition = True
    elif type_of_fire == 'Medium':
        if 51 <= cells <= 80:
            condition = True
    elif type_of_fire == 'Low':
        if 1 <= cells <= 50:
            condition = True

    if condition:
        if water_amount >= cells:
            water_amount -= cells
            effort += cells * 0.25
            total_fire += cells
            print(f" - {cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")