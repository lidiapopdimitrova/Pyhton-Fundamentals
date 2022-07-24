month = input()
number_of_nights = int(input())
price_for_studio = 0
price_for_apartment = 0

if month == 'May' or month == 'October':
    price_for_studio += 50
    price_for_apartment += 65
    if 7 < number_of_nights < 14:
        price_for_studio *= 0.95
    elif number_of_nights > 14:
        price_for_studio *= 0.7
        price_for_apartment *= 0.9

elif month == 'June' or month == 'September':
    price_for_studio += 75.20
    price_for_apartment += 68.70
    if number_of_nights > 14:
        price_for_studio *= 0.8
        price_for_apartment *= 0.9

elif month == 'July' or month == 'August':
    price_for_studio += 76
    price_for_apartment += 77
    if number_of_nights > 14:
        price_for_apartment *= 0.9

total_for_studio = price_for_studio * number_of_nights
total_for_apartment = price_for_apartment * number_of_nights
print(f"Apartment: {total_for_apartment:.2f} lv.")
print(f"Studio: {total_for_studio:.2f} lv.")

