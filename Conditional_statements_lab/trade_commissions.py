city = input()
profit = float(input())
commission = 0
if city not in 'Sofia Varna Plovdiv':
    print('error')

if city == 'Sofia':
    if 0 <= profit <= 500:
        commission = profit * 0.05
        print(f'{commission:.2f}')
    elif 500 < profit <= 1000:
        commission = profit * 0.07
        print(f'{commission:.2f}')
    elif 1000 < profit <= 10000:
        commission = profit * 0.08
        print(f'{commission:.2f}')
    elif profit > 10000:
        commission = profit * 0.12
        print(f'{commission:.2f}')
    else:
        print('error')


if city == 'Varna':
    if 0 <= profit <= 500:
        commission = profit * 0.045
        print(f'{commission:.2f}')
    elif 500 < profit <= 1000:
        commission = profit * 0.075
        print(f'{commission:.2f}')
    elif 1000 < profit <= 10000:
        commission = profit * 0.1
        print(f'{commission:.2f}')
    elif profit > 10000:
        commission = profit * 0.13
        print(f'{commission:.2f}')
    else:
        print('error')



if city == 'Plovdiv':
    if 0 <= profit <= 500:
        commission = profit * 0.055
        print(f'{commission:.2f}')
    elif 500 < profit <= 1000:
        commission = profit * 0.08
        print(f'{commission:.2f}')
    elif 1000 < profit <= 10000:
        commission = profit * 0.12
        print(f'{commission:.2f}')
    elif profit > 10000:
        commission = profit * 0.145
        print(f'{commission:.2f}')
    else:
        print('error')


