targets = list(map(int, input().split()))
while True:
    word = input()
    if word == "End":
        break

    tokens = word.split()
    command = tokens[0]
    index = int(tokens[1])
    value = int(tokens[2])

    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
        continue
    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index < len(targets) - 1:
            start = index - value
            end = index + value

            if start >= 0 and end < len(targets):
                del targets[start: end + 1]
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")

res = [str(target) for target in targets]
print("|".join(res))
