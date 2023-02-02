words = input()

word_dict = {}

for char in words:
    if char.isspace():
        continue
    if char not in word_dict:
        word_dict[char] = 1
    else:
        word_dict[char] += 1

for key, value in word_dict.items():
    print(f"{key} -> {value}")