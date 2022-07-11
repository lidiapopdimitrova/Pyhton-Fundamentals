data = input().split()
products = {}

for index in range(0, len(data), 2):
    product = data[index]
    quantity = int(data[index + 1])
    products[product] = quantity

print(products)