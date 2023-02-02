pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health_capacity = int(input())
stop_game = False
while True:
    word = input()
    if word == "Retire":
        break
    tokens = word.split()

    command = tokens[0]
    if command == "Fire":
        fire_index = int(tokens[1])
        fire_dmg = int(tokens[2])

        if 0 <= fire_index < len(warship):
            warship[fire_index] -= fire_dmg
            if warship[fire_index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()
                # break

        else:

            continue

    elif command == "Defend":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        def_dmg = int(tokens[3])

        if start_index >= 0 and end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= def_dmg

                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    # break
                    exit()

    elif command == "Repair":
        repair_index = int(tokens[1])
        health = int(tokens[2])

        if 0 <= repair_index < len(pirate_ship):
            pirate_ship[repair_index] += health
            if pirate_ship[repair_index] > max_health_capacity:
                pirate_ship[repair_index] = max_health_capacity

    elif command == "Status":
        need_repair = max_health_capacity * 0.2
        repair_count = []
        for n in pirate_ship:
            if n < need_repair:
                repair_count.append(n)
        print(f"{len(repair_count)} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
