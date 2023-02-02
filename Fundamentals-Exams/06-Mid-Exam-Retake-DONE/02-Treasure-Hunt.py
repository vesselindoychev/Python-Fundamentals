treasure_chest = input().split("|")

command = input()

while not command == "Yohoho!":

    if "Loot" in command:
        loot = command.split()
        loot.remove("Loot")
        for w in loot:
            if w not in treasure_chest:
                treasure_chest.insert(0, w)

    elif "Drop" in command:
        drop = command.split()
        index = int(drop[1])

        if 0 <= index < len(treasure_chest):
            x = treasure_chest[index]
            treasure_chest.remove(x)
            treasure_chest.append(x)

    elif "Steal" in command:
        steal = command.split()
        count = int(steal[1])
        stolen_items = []

        for _ in range(count):
            if not treasure_chest:
                break
            stolen_items.append(treasure_chest.pop())

        stolen_items.reverse()
        print(*stolen_items, sep=", ")

    command = input()

if treasure_chest:
    length = ''.join(treasure_chest)
    average_gain = len(length) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")
