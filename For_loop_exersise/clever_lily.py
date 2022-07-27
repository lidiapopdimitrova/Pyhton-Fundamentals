age = int(input())
price_of_machine = float(input())
price_of_a_toy = int(input())
number_of_toys = 0
total = 0
money_for_birthday = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_for_birthday += 10
        total += money_for_birthday - 1
    else:
        number_of_toys += 1

total += number_of_toys * price_of_a_toy
diff = abs(total - price_of_machine)
if total >= price_of_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")