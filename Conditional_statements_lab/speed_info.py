speed_number = float(input())

if speed_number <= 10:
    print('slow')
elif 10 < speed_number <= 50:
    print('average')

elif 50 < speed_number <= 150:
    print('fast')

elif 150 < speed_number <= 1000:
    print('ultra fast')

else:
    print('extremely fast')
