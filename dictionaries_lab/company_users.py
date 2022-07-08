data = input()
companies = dict()

while data != "End":
    name, id_user = data.split(" -> ")
    if name not in companies:
        companies[name] = []
    if id_user not in companies[name]:
        companies[name].append(id_user)

    data = input()

for names, users in companies.items():
    print(f"{names}")
    for user in companies[names]:
        print(f"-- {user}")
