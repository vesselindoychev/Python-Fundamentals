fire_str = input().split("#")
amount_of_water = int(input())

fires = []
for fire in fire_str:
    tokens = fire.split(" = ")

    fire_type = tokens[0]
    cell_value = int(tokens[1])

    if fire_type == "High" and 81 <= cell_value <= 125:
        fires.append(cell_value)

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        fires.append(cell_value)

    elif fire_type == "Low" and 1 <= cell_value <= 50:
        fires.append(cell_value)

    else:
        continue

effort = 0
total_fire = 0
cells = []
for j in fires:
    if amount_of_water >= j:
        amount_of_water -= j
        effort += j * 0.25
        total_fire += j
        cells.append(j)
    else:
        continue
print(f"Cells:")

for i in cells:
    print(f" - {i}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
