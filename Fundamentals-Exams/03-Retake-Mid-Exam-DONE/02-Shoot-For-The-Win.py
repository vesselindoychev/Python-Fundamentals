targets = list(map(int, input().split()))

shot_targets_counter = 0

while True:
    command = input()
    if command == "End":
        break

    index = int(command)

    if 0 <= index < len(targets):
        temp_number = targets[index]

        for i in range(len(targets)):
            if not targets[i] == -1:
                if targets[i] > temp_number:
                    targets[i] -= temp_number
                else:
                    targets[i] += temp_number

        targets[index] = -1
        shot_targets_counter += 1

print(f"Shot targets: {shot_targets_counter} -> {' '.join(map(str, targets))}")