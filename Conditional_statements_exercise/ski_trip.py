number_of_days = int(input())
type_of_room = input()
grade = input()
room_for_one_person = 18
apartment = 25
president_apartment = 35
nights_to_pay = number_of_days - 1
total_for_room = room_for_one_person * nights_to_pay
total_for_apartment = apartment * nights_to_pay
total_for_president = president_apartment * nights_to_pay

if number_of_days < 10:
    if type_of_room == 'apartment':
        total_for_apartment *= 0.7
    elif type_of_room == 'president apartment':
        total_for_president *= 0.9


elif 10 < number_of_days < 15:
    if type_of_room == 'apartment':
        total_for_apartment *= 0.65
    elif type_of_room == 'president apartment':
        total_for_president *= 0.85

elif number_of_days > 15:
    if type_of_room == 'apartment':
        total_for_apartment *= 0.5
    elif type_of_room == 'president apartment':
        total_for_president *= 0.8

if grade == 'positive':
    total_for_apartment += total_for_apartment * 0.25
    total_for_room += total_for_room * 0.25
    total_for_president += total_for_president * 0.25
elif grade == 'negative':
    total_for_apartment -= total_for_apartment * 0.1
    total_for_room -= total_for_room * 0.1
    total_for_president -= total_for_president * 0.1

if type_of_room == 'apartment':
    print(f"{total_for_apartment:.2f}")
elif type_of_room == 'president apartment':
    print(f"{total_for_president:.2f}")
elif type_of_room == 'room for one person':
    print(f"{total_for_room:.2f}")
