events = input().split("|")

energy = 100
coins = 100
is_bankrupt = False
for event in events:
    tokens = event.split("-")
    name = tokens[0]
    value = int(tokens[1])

    if name == "rest":
        gained_energy = 0

        if value + energy < 100:
            gained_energy = value
            energy += value
        else:
            gained_energy = 100 - energy
            energy = 100

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif name == "order":

        if energy - 30 > 0:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
            continue

    else:
        ingredient = name

        if coins >= value:
            coins -= value
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            is_bankrupt = True

if not is_bankrupt:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
