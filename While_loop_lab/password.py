name = input()
password = input()

while True:
    current_password = input()
    if current_password == password:
        print(f"Welcome {name}!")
        break

