import re

n = int(input())
matches = []
valid_matches = []
new_matches = []
for i in range(n):
    text = input()

    for letter in text:
        if "%" in text:
            percent_index = text.index("%")
            if percent_index == 0:
                matches.append(text)
            else:
                print(f"Valid message not found!")

            break

        else:
            dollar_index = text.index("$")
            if dollar_index == 0:
                matches.append(text)
            else:
                print(f"Valid message not found!")
            break
for string in matches:
    tokens = string.split(": ")
    tag = tokens[0]
    data = tokens[1]
    pattern = r"(%|\$)[A-Z][a-z]{2,}\1:\s(\[\d+\]\|){3}($|(?=\s))"
    valid_matches = [obj.group() for obj in re.finditer(pattern, string)]
    if valid_matches:
        new_tag = tag[1:-1]

        index = 0
        current_num = ""
        while index < len(data) - 1:
            if data[index].isdigit():
                current_num += data[index]
                index += 1
                print(f"{tag}: {chr(int(current_num))}")
                if not data[index].isdigit():
                    current_num = ""
                    index += 1
            else:
                index += 1

    else:
        print(f"Valid message not found!")

# print(matches)
# print(valid_matches)
