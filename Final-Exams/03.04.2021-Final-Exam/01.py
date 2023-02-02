mail = input()

ascii_values = []
text = input()
while not text == "Complete":
    tokens = text.split()

    command = tokens[0]

    if command == "Make":
        if tokens[1] == "Upper":
            mail = mail.upper()

        elif tokens[1] == "Lower":
            mail = mail.lower()
        print(mail)
    elif command == "GetDomain":
        count = int(tokens[1])
        last_count_letters = mail[len(mail) - count:]
        print(last_count_letters)

    elif command == "GetUsername":
        if "@" not in mail:
            print(f"The email {mail} doesn't contain the @ symbol.")
        else:
            at_symbol = mail.index("@")
            print(mail[:at_symbol])

    elif command == "Replace":
        char = tokens[1]
        mail = mail.replace(char, "-")
        print(mail)

    elif command == "Encrypt":
        # mail = mail.replace(mail[-1], "")
        for letter in mail:
            letter = ord(letter)
            ascii_values.append(letter)

        print(*ascii_values)

    text = input()
