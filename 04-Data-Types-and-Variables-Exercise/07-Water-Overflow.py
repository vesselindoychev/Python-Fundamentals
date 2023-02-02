n = int(input())

CAPACITY = 255
water_tank = 0
for i in range(1, n + 1):
    quantities_water = int(input())

    water_tank += quantities_water

    if water_tank > CAPACITY:
        water_tank -= quantities_water
        print("Insufficient capacity!")
print(water_tank)

