type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())
price_per_flower = 0


if type_of_flower == 'Roses':
    price_per_flower += 5
    total = number_of_flowers * price_per_flower
    if number_of_flowers > 80:
        total = total * 0.9
elif type_of_flower == 'Dahlias':
    price_per_flower += 3.8
    total = number_of_flowers * price_per_flower
    if number_of_flowers > 90:
        total = total * 0.85
elif type_of_flower == 'Tulips':
    price_per_flower += 2.8
    total = number_of_flowers * price_per_flower
    if number_of_flowers > 80:
        total = total * 0.85
elif type_of_flower == 'Narcissus':
    price_per_flower += 3
    total = number_of_flowers * price_per_flower
    if number_of_flowers < 120:
        total = total + total * 0.15
elif type_of_flower == 'Gladiolus':
    price_per_flower += 2.5
    total = number_of_flowers * price_per_flower
    if number_of_flowers < 80:
        total = total + total * 0.2

absolut = abs(budget - total)

if budget >= total:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {absolut:.2f} leva left.")
elif budget < total:
    print(f"Not enough money, you need {absolut:.2f} leva more.")
