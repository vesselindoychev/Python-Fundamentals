password = input()

text = input()
while not text == "Done":
    tokens = text.split(" ")
    command = tokens[0]

    sibling_pass = password
    if command == "TakeOdd":
        password = ""
        for i in range(len(sibling_pass)):
            if i % 2 != 0:
                password += sibling_pass[i]

        print(password)

    elif command == "Cut":
        index = int(tokens[1])
        length = int(tokens[2])

        password = password.replace(password[index: index + length], "", 1)
        print(password)

    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")

    text = input()

print(f"Your password is: {password}")