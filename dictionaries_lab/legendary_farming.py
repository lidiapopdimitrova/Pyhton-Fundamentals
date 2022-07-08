data = input()
items = {"shards": 0, "fragments": 0, "motes": 0}
junk = dict()

key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

is_obtained = False

while not is_obtained:
    split_data = data.split()

    for index in range(0, len(split_data), 2):
        if is_obtained:
            break

        quantity = int(split_data[index])
        material = split_data[index + 1].lower()

        if material in items:
            items[material] += quantity
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

        for material, quantity in items.items():
            if quantity >= 250:
                is_obtained = True
                items[material] -= 250
                print(f"{key_materials[material]} obtained!")
                break

    if is_obtained:
        break

    data = input()

# sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

print(f"shards: {items['shards']}")
print(f"fragments: {items['fragments']}")
print(f"motes: {items['motes']}")


# sorted_junks = sorted(junk.items(), key=lambda kvp: kvp[0])
for material, quantity in junk.items():
    print(f"{material}: {quantity}")