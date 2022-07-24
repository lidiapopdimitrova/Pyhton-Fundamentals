budget = float(input())
season = input()
destination = ''
place = ''
cost = 0
if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        cost = budget * 0.3
        destination = 'Camp'
    elif season == 'winter':
        cost = budget * 0.7
        destination = 'Hotel'
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        cost = budget * 0.4
        destination = 'Camp'
    elif season == 'winter':
        cost = budget * 0.8
        destination = 'Hotel'
elif budget > 1000:
    place = 'Europe'
    cost = budget * 0.9
    destination = 'Hotel'

print(f"Somewhere in {place}.")
print(f"{destination} - {cost:.2f}")
