num = int(input())
pieces = dict()

for i in range(num):
    data = input().split("|")
    if data[0] == "Add":
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece not in pieces:

    elif data[0] == "Remove":
        pass
    elif data[0] == "ChangeKey":
        pass
    else:
        pass
