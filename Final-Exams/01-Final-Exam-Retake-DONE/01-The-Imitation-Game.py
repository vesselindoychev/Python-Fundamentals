text = input()

commands = input()
while not commands == "Decode":
    tokens = commands.split("|")

    command = tokens[0]

    if command == "Move":
        n_letters = int(tokens[1])
        letters_to_change = text[:n_letters]
        text = text.replace(letters_to_change, "")
        text = text + letters_to_change

    elif command == "Insert":
        index = int(tokens[1])
        value = tokens[2]
        first_part = text[:index]
        second_part = text[index:]
        text = first_part + value + second_part

    elif command == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]

        text = text.replace(substring, replacement)

    commands = input()

print(f"The decrypted message is: {text}")