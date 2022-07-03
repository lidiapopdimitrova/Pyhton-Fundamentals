number = int(input())
sum_num = 0

while sum_num < number:
    current_number = int(input())
    sum_num += current_number
    if sum_num >= number:
        print(sum_num)
        break
