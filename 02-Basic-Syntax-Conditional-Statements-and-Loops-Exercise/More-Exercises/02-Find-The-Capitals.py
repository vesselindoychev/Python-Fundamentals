text = input()

indices = []
index_of_char= 0
for i in text:
    if i.isupper():
        indices.append(index_of_char)
    index_of_char += 1
print(indices)