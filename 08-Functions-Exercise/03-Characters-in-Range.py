def character_in_range(first_char, last_char):
    for i in range(ord(first_char) + 1, ord(last_char)):
        print(chr(i), end=" ")


first_char = input()
last_char = input()
character_in_range(first_char, last_char)