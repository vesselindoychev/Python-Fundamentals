words = input().split()

elements = {}

for word in words:
    word = word.lower()
    if word not in elements:
        elements[word] = 1
    else:
        elements[word] += 1

for key, value in elements.items():
    if value % 2 != 0:
        print(key, end=" ")