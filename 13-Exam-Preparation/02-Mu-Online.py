dungeon_rooms = input().split("|")

is_alive = True
health = 100
bitcoins = 0
total_bitcoins = 0
for dungeon_room in dungeon_rooms:
    tokens = dungeon_room.split()
    command = tokens[0]
    number = int(tokens[1])

    if command == "potion":
        temp = health
        health += number
        healed_part = number

        if health > 100:
            health = 100
            healed_part = 100 - temp

        print(f"You healed for {healed_part} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        total_bitcoins += number
        bitcoins = number
        print(f"You found {bitcoins} bitcoins.")

    else:
        health -= number

        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {dungeon_rooms.index(dungeon_room) + 1}")
            is_alive = False
            break

if is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {total_bitcoins}")
    print(f"Health: {health}")