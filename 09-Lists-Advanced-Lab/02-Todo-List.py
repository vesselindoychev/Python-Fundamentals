notes = []

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-", maxsplit=1)
    priority = int(tokens[0])
    task = tokens[1]

    notes.append((priority, task))

task_as_priority = [task_name for priority, task_name in sorted(notes)]
print(task_as_priority)
