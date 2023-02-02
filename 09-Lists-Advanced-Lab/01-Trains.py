wagons = int(input())
wagons_length = []

for i in range(wagons):

    wagons_length.append(0)

while True:
    command = input()
    tokens = command.split()

    if command == "End":
        break
    command = tokens[0]
    index = int(tokens[1])

    if command == "add":
        people_to_add = int(tokens[1])
        wagons_length[-1] += people_to_add

    elif command == "insert":
        people_to_insert = int(tokens[2])
        wagons_length[index] += people_to_insert

    elif command == "leave":
        people_to_leave = int(tokens[2])
        wagons_length[index] -= people_to_leave

print(wagons_length)