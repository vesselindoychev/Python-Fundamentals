groceries_list = input().split("!")

while True:
    text = input()

    if text == "Go Shopping!":
        break

    tokens = text.split()

    command = tokens[0]
    item = tokens[1]

    if command == "Urgent":
        if item in groceries_list:
            continue
        groceries_list.insert(0, item)

    elif command == "Unnecessary":
        if item not in groceries_list:
            continue
        groceries_list.remove(item)

    elif command == "Correct":
        old_item = tokens[1]
        new_item = tokens[2]
        if old_item not in groceries_list:
            continue
        old_item_index = groceries_list.index(old_item)
        groceries_list.insert(old_item_index, new_item)
        groceries_list.remove(old_item)

    elif command == "Rearrange":
        if item not in groceries_list:
            continue
        groceries_list.remove(item)
        groceries_list.append(item)

print(", ".join(groceries_list))
