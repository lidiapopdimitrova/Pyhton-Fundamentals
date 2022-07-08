entry = input()
contacts = dict()

while not entry.isnumeric():
    name, number = entry.split("-")
    if name not in contacts:
        contacts[name] = number
    contacts[name] = number

    entry = input()


for i in range(int(entry)):
    phone_name = input()
    if phone_name not in contacts:
        print(f"Contact {phone_name} does not exist.")
    else:
        print(f"{phone_name} -> {contacts[phone_name]}")

