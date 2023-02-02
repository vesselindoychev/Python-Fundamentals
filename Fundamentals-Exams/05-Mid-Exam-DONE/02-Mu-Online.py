rooms = input().split("|")
health = 100
bitcoins = 0
for room in rooms:
    tokens = room.split()
    command = tokens[0]
    value = int(tokens[1])

    if command == "potion":
        twin_health = health
        health += value
        healed_part = value
        if health > 100:
            healed_part = 100 - twin_health
            health = 100

        print(f"You healed for {healed_part} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")