text = input()


index = 0

while index < len(text) - 1:
    if text[index] == text[index + 1]:
        char_to_replace = f"{text[index]}{text[index + 1]}"
        text = text.replace(char_to_replace, text[index])
        index = 0

    else:
        index += 1
print(text)