energy = int(input())

command = input()
win_tracker = 0
while not command == "End of battle":
    distance = int(command)

    if energy >= distance:
        energy -= distance
        win_tracker += 1
        if win_tracker % 3 == 0:
            energy += win_tracker
    else:

        print(f"Not enough energy! Game ends with {win_tracker} won battles and {energy} energy")
        break

    command = input()

if command == "End of battle":
    print(f"Won battles: {win_tracker}. Energy left: {energy}")
