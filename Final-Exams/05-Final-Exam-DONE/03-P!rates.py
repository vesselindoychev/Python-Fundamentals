sail_command = input()

cities_info = {}
while not sail_command == "Sail":
    tokens = sail_command.split("||")

    city = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])

    if city not in cities_info:
        cities_info[city] = {"population": population, "gold": gold}
    else:
        cities_info[city]["population"] += population
        cities_info[city]["gold"] += gold
    sail_command = input()

end_command = input()
while not end_command == "End":
    events = end_command.split("=>")
    command = events[0]
    initial_city = events[1]

    if command == "Plunder":
        initial_people = int(events[2])
        initial_gold = int(events[3])

        if initial_city in cities_info:
            cities_info[initial_city]["population"] -= initial_people
            cities_info[initial_city]["gold"] -= initial_gold
            print(f"{initial_city} plundered! {initial_gold} gold stolen, {initial_people} citizens killed.")
            if cities_info[initial_city]["population"] <= 0 or cities_info[initial_city]["gold"] <= 0:
                cities_info.pop(initial_city)
                print(f"{initial_city} has been wiped off the map!")

    elif command == "Prosper":
        initial_gold = int(events[2])

        if initial_city in cities_info:
            if initial_gold > 0:
                cities_info[initial_city]["gold"] += initial_gold
                print(f"{initial_gold} gold added to the city treasury."
                      f" {initial_city} now has {cities_info[initial_city]['gold']} gold.")
            else:
                print(f"Gold added cannot be a negative number!")

    end_command = input()


sorted_data = sorted(cities_info.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0]))
if len(cities_info) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for key, value in sorted_data:
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
