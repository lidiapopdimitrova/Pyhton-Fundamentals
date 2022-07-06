bought_items = input().split('|')
budget = float(input())
condition = False
profit = 0
profited_money = 0
new_prices_list = []
for items in bought_items:
    item_data = items.split('->')
    type_of_clothing = item_data[0]
    start_price = float(item_data[1])
    condition = False

    if type_of_clothing == 'Clothes':
        if start_price <= 50:
            condition = True
    elif type_of_clothing == 'Shoes':
        if start_price <= 35:
            condition = True
    elif type_of_clothing == 'Accessories':
        if start_price <= 20.50:
            condition = True
    if condition:
        if budget >= start_price:
            budget -= start_price
            profit += start_price * 0.4
            new_price = start_price + start_price * 0.4
            profited_money += start_price + profit
            new_prices_list.append(f"{new_price:.2f}")
print(" ".join(new_prices_list))


print(f"Profit: {profit:.2f}")

if (budget + profited_money) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

