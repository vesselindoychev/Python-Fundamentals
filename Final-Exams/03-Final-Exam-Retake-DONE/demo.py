n = int(input())

auto_house = {}
for _ in range(n):
    cars = input().split("|")
    car = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])

    if car not in auto_house:
        auto_house[car] = {"mileage": mileage, "fuel": fuel}

text = input()
while not text == "Stop":
    tokens = text.split(" : ")
    command = tokens[0]
    initial_car = tokens[1]

    if command == "Drive":
        distance = int(tokens[2])
        initial_fuel = int(tokens[3])

        if auto_house[initial_car]["fuel"] >= initial_fuel:
            auto_house[initial_car]["mileage"] += distance
            auto_house[initial_car]["fuel"] -= initial_fuel
            print(f"{initial_car} driven for {distance} kilometers. {initial_fuel} liters of fuel consumed.")

            if auto_house[initial_car]["mileage"] >= 100_000:
                auto_house.pop(initial_car)
                print(f"Time to sell the {initial_car}!")
        else:
            print(f"Not enough fuel to make that ride")

    elif command == "Refuel":
        refill_fuel = int(tokens[2])
        needed_fuel = 0
        if refill_fuel + auto_house[initial_car]["fuel"] > 75:
            needed_fuel = 75 - auto_house[initial_car]["fuel"]
            auto_house[initial_car]["fuel"] = 75
            print(f"{initial_car} refueled with {needed_fuel} liters")
        else:
            auto_house[initial_car]["fuel"] += refill_fuel
            print(f"{initial_car} refueled with {refill_fuel} liters")

    elif command == "Revert":
        kilometers = int(tokens[2])

        if auto_house[initial_car]["mileage"] - kilometers >= 10_000:
            auto_house[initial_car]["mileage"] -= kilometers
            print(f"{initial_car} mileage decreased by {kilometers} kilometers")
        else:
            auto_house[initial_car]["mileage"] = 10_000

    text = input()

sorted_auto_house = sorted(auto_house.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0]))

for key, value in sorted_auto_house:
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")