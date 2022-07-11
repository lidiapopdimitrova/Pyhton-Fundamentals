data = input().split()
products = {}

for i in range(0, len(data), 2):
    current_product = data[i]
    quantity = int(data[i + 1])
    products[current_product] = quantity


searched_products = input().split()
for s_product in searched_products:
    if s_product in products:
        print(f"We have {products[s_product]} of {s_product} left")
    else:
        print(f"Sorry, we don't have {s_product}")
