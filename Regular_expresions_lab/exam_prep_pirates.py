cities = input()
info_cities = dict()

while cities != "Sail":
    city_details = cities.split("||")
    name = city_details[0]
    population = int(city_details[1])
    gold = int(city_details[2])
    current_city_dict = dict()
    current_city_dict["population"] = population
    current_city_dict["gold"] = gold

    if name not in info_cities:
        info_cities[name] = current_city_dict
    else:
        info_cities[name]["population"] += population
        info_cities[name]["gold"] += gold

    cities = input()

events = input()
while events != "End":
    events_pieces = events.split("=>")

    if events_pieces[0] == "Plunder":
        town = events_pieces[1]
        people = int(events_pieces[2])
        money = int(events_pieces[3])
        info_cities[town]["population"] -= people
        info_cities[town]["gold"] -= money
        print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")

        if info_cities[town]["population"] == 0 or info_cities[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            del info_cities[town]

    elif events_pieces[0] == "Prosper":
        town = events_pieces[1]
        added_gold = int(events_pieces[2])
        if added_gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            info_cities[town]["gold"] += added_gold
            print(f"{added_gold} gold added to the city treasury. {town} now has {info_cities[town]['gold']} gold.")

    events = input()

print(f"Ahoy, Captain! There are {len(info_cities)} wealthy settlements to go to:")
if len(info_cities) > 0:
    for town in info_cities:
        print(f"{town} -> Population: {info_cities[town]['population']} citizens, Gold: {info_cities[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

