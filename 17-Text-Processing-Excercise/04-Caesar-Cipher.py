text = input()
res = []
for char in text:
    char = ord(char) + 3
    char = chr(char)
    res.append(char)

print(''.join(res))
