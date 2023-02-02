inventory = input().split(", ")

while True:
    arg = input()
    if arg == "Craft!":
        break

    tokens = arg.split(" - ")
    command = tokens[0]
    item = tokens[1]

    if command == "Collect":

        if item in inventory:
            continue
        inventory.append(item)

    elif command == "Drop":

        if item in inventory:
            inventory.remove(item)
        else:
            continue

    elif command == "Combine Items":

        items = item.split(":")
        old_item = items[0]
        new_item = items[1]

        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)

        else:
            continue
    else:
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))

print(", ".join(inventory))
