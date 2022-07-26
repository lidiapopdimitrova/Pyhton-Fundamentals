product = input()
city = input()
quantity = float(input())

if city == 'Sofia':
    if product == 'coffee':
        total = quantity * 0.50
    elif product == 'water':
        total = quantity * 0.80
    elif product == 'sweets':
        total = quantity * 1.45
    elif product == 'beer':
        total = quantity * 1.20
    elif product == 'peanuts':
        total = quantity * 1.60

if city == 'Plovdiv':
    if product == 'coffee':
        total = quantity * 0.40
    elif product == 'water':
        total = quantity * 0.70
    elif product == 'sweets':
        total = quantity * 1.30
    elif product == 'beer':
        total = quantity * 1.15
    elif product == 'peanuts':
        total = quantity * 1.50

if city == 'Varna':
    if product == 'coffee':
        total = quantity * 0.45
    elif product == 'water':
        total = quantity * 0.70
    elif product == 'sweets':
        total = quantity * 1.35
    elif product == 'beer':
        total = quantity * 1.10
    elif product == 'peanuts':
        total = quantity * 1.55
print(total)
