n = int(input())

plant_discovery = {}
for _ in range(n):
    text = input().split("<->")
    plant_name = text[0]
    rarity = int(text[1])

    if plant_name not in plant_discovery:
        plant_discovery[plant_name] = {"rarity": rarity, "rating": []}

commands = input()
while not commands == "Exhibition":
    tokens = commands.split(": ")
    command = tokens[0]
    operations = tokens[1]

    if command == "Rate":
        split_data = operations.split(" - ")
        initial_plant = split_data[0]
        rating = int(split_data[1])

        if initial_plant in plant_discovery:
            plant_discovery[initial_plant]["rating"].append(rating)
        else:
            print("error")
    elif command == "Update":
        split_data = operations.split(" - ")
        initial_plant = split_data[0]
        new_rarity = int(split_data[1])
        if initial_plant in plant_discovery:
            plant_discovery[initial_plant]["rarity"] = new_rarity
        else:
            print("error")
    elif command == "Reset":
        split_data = operations.split(" - ")
        initial_plant = split_data[0]
        if initial_plant in plant_discovery:
            plant_discovery[initial_plant]["rating"].clear()
        else:
            print("error")
    else:
        print(f"error")

    commands = input()


for key, value in plant_discovery.items():
    if value["rating"] == []:
        average_points = 0

    else:
        average_points = sum(value["rating"]) / len(value["rating"])
    plant_discovery[key]["avg"] = average_points

sorted_plants = sorted(plant_discovery.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["avg"]))

print(f"Plants for the exhibition:")

for k, v in sorted_plants:
    print(f"- {k}; Rarity: {v['rarity']}; Rating: {v['avg']:.2f}")