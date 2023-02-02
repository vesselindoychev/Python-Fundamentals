raw_key = input()

text = input()
while not text == "Generate":
    tokens = text.split(">>>")
    command = tokens[0]

    if command == "Contains":
        substring = tokens[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        start_index = int(tokens[2])
        end_index = int(tokens[3])
        if tokens[1].startswith("Upper"):
            upper_case = raw_key[start_index: end_index].upper()
            raw_key = raw_key.replace(raw_key[start_index: end_index], upper_case)
        else:
            lower_case = raw_key[start_index: end_index].lower()
            raw_key = raw_key.replace(raw_key[start_index: end_index], lower_case)
        print(raw_key)

    elif command == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        raw_key = raw_key.replace(raw_key[start_index: end_index], "")
        print(raw_key)
    text = input()

print(f"Your activation key is: {raw_key}")