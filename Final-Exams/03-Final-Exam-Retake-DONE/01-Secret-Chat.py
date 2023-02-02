text = input()

while True:
    message = input()
    if message == "Reveal":
        break
    tokens = message.split(":|:")
    command = tokens[0]

    if command == "InsertSpace":
        given_index = int(tokens[1])

        text = text[:given_index] + " " + text[given_index:]
        print(text)
    elif command == "Reverse":
        given_substring = tokens[1]

        if given_substring in text:
            text = text.replace(given_substring, "", 1)
            reversed_substring = given_substring[::-1]
            text = text + reversed_substring
            print(text)
        else:
            print(f"error")

    elif command == "ChangeAll":
        replace = tokens[1]
        replace_with = tokens[2]

        text = text.replace(replace, replace_with)
        print(text)

print(f"You have a new text message: {text}")