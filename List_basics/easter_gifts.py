gift_names = input().split()
command = input().split()
command_name = command[0]
gift = command[1]

while command[0] != 'No' and command[1] != 'Money':

    if command[0] == 'OutOfStock':
        if command[1] in gift_names:
            for i in range(len(gift_names)):
                if gift_names[i] == command[1]:
                    gift_names[i] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gift_names):
            gift_names[index] = command[1]

    elif command[0] == 'JustInCase':
        gift_names[-1] = command[1]

    command = input().split()


while 'None' in gift_names:
    gift_names.remove('None')

for y in gift_names:
    print(y, end=' ')
