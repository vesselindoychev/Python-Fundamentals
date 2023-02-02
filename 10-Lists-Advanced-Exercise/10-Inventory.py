inventory = input().split(", ")

while True:
    word = input()

    if word == "Craft!":
        break

    tokens = word.split(" - ")
    command = tokens[0]
    item = tokens[1]

    if command == "Collect":
        if item in inventory:
            continue
        inventory.append(item)

    elif command == "Drop":
        if item not in inventory:
            continue
        inventory.remove(item)

    elif command == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]

        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
        continue

    elif command == "Renew":
        if item not in inventory:
            continue
        inventory.remove(item)
        inventory.append(item)

print(", ".join(inventory))