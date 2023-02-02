def is_index_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False


text = input()

commands = input()
while not commands == "Travel":
    tokens = commands.split(":")
    command = tokens[0]

    if command.startswith("Add"):
        index = int(tokens[1])
        string = tokens[2]

        if is_index_valid(index, text):
            text = text[:index] + string + text[index:]

    elif command.startswith("Remove"):
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if is_index_valid(start_index, text) and is_index_valid(end_index, text):
            string_to_replace = text[start_index: end_index + 1]
            text = text.replace(string_to_replace, "")

    elif command == "Switch":
        old_string = tokens[1]
        new_string = tokens[2]

        if old_string in text:
            text = text.replace(old_string, new_string)

    print(text)
    commands = input()

print(f"Ready for world tour! Planned stops: {text}")
