start = int(input())
finish = int(input())
filtered = []
for index in range(start, start * finish + 1, start):
    filtered.append(index)
print(filtered)