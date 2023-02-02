def password_validator(password):
    is_valid = True
    counter = 0
    if len(password) > 10 or len(password) < 6:
        is_valid = False
        print(f"Password must be between 6 and 10 characters")

    for element in password:
        if element.isdigit():
            counter += 1

    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    if counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


password = input()
result = password_validator(password)

if result:
    print("Password is valid")