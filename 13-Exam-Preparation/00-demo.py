collecting_items = input().split(", ")

while True:
    arg = input()

    if arg == "Craft!":
        break

    tokens = arg.split(" - ")
    command = tokens[0]
    item = tokens[1]

    if command == "Collect":
        if item in collecting_items:
            continue
        collecting_items.append(item)

    elif command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
        else:
            continue

    elif command == "Combine Items":
        items = item.split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in collecting_items:
            old_item_index = collecting_items.index(old_item)

            collecting_items.insert(old_item_index + 1, new_item)
        else:
            continue
    else:
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)
print(", ".join(collecting_items))
