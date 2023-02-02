n = int(input())

car_data = {}
for n_cars in range(n):
    initial_text = input().split("|")

    initial_car = initial_text[0]
    initial_mileage = int(initial_text[1])
    initial_fuel = int(initial_text[2])
    if initial_car not in car_data:
        car_data[initial_car] = {"Mileage": initial_mileage, "Fuel": initial_fuel}

car_text = input()
while not car_text == "Stop":
    tokens = car_text.split(" : ")
    command = tokens[0]
    car = tokens[1]
    if command == "Drive":
        distance = int(tokens[2])
        fuel = int(tokens[3])

        if car_data[car]["Fuel"] > fuel:
            car_data[car]["Mileage"] += distance
            car_data[car]["Fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_data[car]["Mileage"] >= 100000:
                car_data.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print(f"Not enough fuel to make that ride")

    elif command == "Refuel":
        re_fuel = int(tokens[2])
        needed_fuel = 0
        if car_data[car]["Fuel"] + re_fuel >= 75:
            needed_fuel = 75 - car_data[car]["Fuel"]
            car_data[car]["Fuel"] = 75
            print(f"{car} refueled with {needed_fuel} liters")
        else:
            car_data[car]["Fuel"] += re_fuel
            needed_fuel = re_fuel
            print(f"{car} refueled with {needed_fuel} liters")

    elif command == "Revert":
        kilometers = int(tokens[2])

        if car_data[car]["Mileage"] - kilometers <= 10_000:
            car_data[car]["Mileage"] = 10_000
        else:
            car_data[car]["Mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    car_text = input()

sorted_data = sorted(car_data.items(), key=lambda kvp: (-kvp[1]["Mileage"], kvp[0]))


for key, value in sorted_data:
    print(f"{key} -> Mileage: {value['Mileage']} kms, Fuel in the tank: {value['Fuel']} lt.")