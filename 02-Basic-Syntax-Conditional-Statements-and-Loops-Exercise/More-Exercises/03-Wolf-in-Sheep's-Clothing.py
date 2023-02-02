animals = input().split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
    exit()
sheep_counter = len(animals)

for wolf in animals:
    sheep_counter -= 1

    if wolf == "wolf":
        print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
        break
