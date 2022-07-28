lenght_in_dm = int(input())
width_in_dm = int(input())
height_in_dm = int(input())
percent = float(input())

bulk = lenght_in_dm * width_in_dm * height_in_dm
bulk_in_liters = bulk * 0.001
taken_place = percent / 100
needed_liters = bulk_in_liters - taken_place * bulk_in_liters

print(needed_liters)

