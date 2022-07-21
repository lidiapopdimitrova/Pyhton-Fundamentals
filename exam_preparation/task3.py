commands = input()
heroes = {}
while commands != "End":
    doings = commands.split()
    if doings[0] == "Enroll":
        hero_name = doings[1]
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif doings[0] == "Learn":
        hero_name = doings[1]
        spell_name = doings[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    elif doings[0] == "Unlearn":
        hero_name = doings[1]
        spell_name = doings[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                heroes[hero_name].remove(spell_name)

    commands = input()


print("Heroes:")

for name, spells in heroes.items():
    print(f"== {name}: {', '.join(spells)}")
