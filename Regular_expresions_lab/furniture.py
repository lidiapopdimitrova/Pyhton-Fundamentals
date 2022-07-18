import re
command = input()
pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"
bought_products = list()
money_spend = 0
while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        bought_products.append(matches.group(1))
        money_spend += float(matches.group(2)) * int(matches.group(3))
    command = input()
print("Bought furniture:")
for match in bought_products:
    print(match)

print(f"Total money spend: {money_spend:.2f}")


