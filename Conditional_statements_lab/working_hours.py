time = int(input())
day = input()

if day in 'Monday Tuesday Wednesday Thursday Friday Saturday' and 10 <= time <= 18:
    print('open')
else:
    print('closed')