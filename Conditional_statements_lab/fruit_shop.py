fruit = input()
day = input()
quantity = float(input())
price = 0

if day not in 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday':
    print('error')

if day in 'Monday Tuesday Wednesday Thursday Friday':
    if fruit == 'apple':
        price = 1.20 * quantity
        print(f"{price:.2f}")
    elif fruit == 'banana':
        price = 2.50 * quantity
        print(f"{price:.2f}")
    elif fruit == 'orange':
        price = 0.85 * quantity
        print(f"{price:.2f}")
    elif fruit == 'grapefruit':
        price = 1.45 * quantity
        print(f"{price:.2f}")
    elif fruit == 'kiwi':
        price = 2.70 * quantity
        print(f"{price:.2f}")
    elif fruit == 'pineapple':
        price = 5.50 * quantity
        print(f"{price:.2f}")
    elif fruit == 'grapes':
        price = 3.85 * quantity
        print(f"{price:.2f}")
    else:
        print('error')

if day in 'Saturday Sunday':
    if fruit == 'apple':
        price = 1.25 * quantity
        print(f"{price:.2f}")
    elif fruit == 'banana':
        price = 2.70 * quantity
        print(f"{price:.2f}")
    elif fruit == 'orange':
        price = 0.90 * quantity
        print(f"{price:.2f}")
    elif fruit == 'grapefruit':
        price = 1.60 * quantity
        print(f"{price:.2f}")
    elif fruit == 'kiwi':
        price = 3.00 * quantity
        print(f"{price:.2f}")
    elif fruit == 'pineapple':
        price = 5.60 * quantity
        print(f"{price:.2f}")
    elif fruit == 'grapes':
        price = 4.20 * quantity
        print(f"{price:.2f}")
    else:
        print('error')
