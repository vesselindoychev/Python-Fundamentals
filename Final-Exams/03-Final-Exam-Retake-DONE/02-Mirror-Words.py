import re

text = input()

pattern = r"(@|#)[a-zA-Z]{3,}\1\1[a-zA-Z]{3,}\1"

matches = [obj.group() for obj in re.finditer(pattern, text)]

valid_pairs = []
for matched_word in matches:
    if matched_word == matched_word[::-1]:
        if "#" in matched_word:
            matched_word = matched_word.replace("#", "")
            valid_pairs.append(matched_word)

        else:
            matched_word = matched_word.replace("@", "")
            valid_pairs.append(matched_word)

data = ""

for valid_pair in valid_pairs:
    for i in range(0, len(valid_pair) // 2):
        data += valid_pair[i]
    data += f"{' '}<=>{' '}"
    for y in range(len(valid_pair) // 2, len(valid_pair)):
        data += valid_pair[y]
    data += f", "

data = data[:-2]

if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
else:
    print(f"No word pairs found!")

if len(valid_pairs) > 0:
    print(f"The mirror words are:")
    print(data)
else:
    print("No mirror words!")
