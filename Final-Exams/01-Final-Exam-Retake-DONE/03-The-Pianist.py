n = int(input())

rhapsody_info = {}

for i in range(n):
    text = input().split("|")
    piece = text[0]
    composer = text[1]
    key = text[2]

    if piece not in rhapsody_info:
        rhapsody_info[piece] = {"composer": composer, "key": key}

commands = input()
while not commands == "Stop":
    tokens = commands.split("|")

    command = tokens[0]
    initial_piece = tokens[1]

    if command == "Add":
        initial_composer = tokens[2]
        initial_key = tokens[3]

        if initial_piece in rhapsody_info:
            print(f"{initial_piece} is already in the collection!")
        else:
            rhapsody_info[initial_piece] = {"composer": initial_composer, "key": initial_key}
            print(f"{initial_piece} by {initial_composer} in {initial_key} added to the collection!")

    elif command == "Remove":
        if initial_piece in rhapsody_info:
            rhapsody_info.pop(initial_piece)
            print(f"Successfully removed {initial_piece}!")
        else:
            print(f"Invalid operation! {initial_piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = tokens[2]

        if initial_piece in rhapsody_info:
            rhapsody_info[initial_piece]["key"] = new_key
            print(f"Changed the key of {initial_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {initial_piece} does not exist in the collection.")

    commands = input()

sorted_rhapsody = sorted(rhapsody_info.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"]))

for key, value in sorted_rhapsody:
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")