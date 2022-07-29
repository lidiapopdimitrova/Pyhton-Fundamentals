n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, n + 1):
    current_num = int(input())
    left_sum += current_num
for i in range(1, n+1):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")

