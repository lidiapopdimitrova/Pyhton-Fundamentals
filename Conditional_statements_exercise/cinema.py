type_of_movie = input()
number_of_columns = int(input())
number_of_lines = int(input())
profit = 0
if type_of_movie == 'Premiere':
    profit = number_of_lines * number_of_columns * 12
elif type_of_movie == 'Normal':
    profit = number_of_lines * number_of_columns * 7.5
else:
    profit = number_of_lines * number_of_columns * 5

print(f"{profit:.2f} leva")
