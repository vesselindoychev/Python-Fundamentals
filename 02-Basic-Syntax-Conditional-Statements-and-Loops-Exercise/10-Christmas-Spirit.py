quantity_decoration = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

spirit = 0
budget = 0
day = 1

while days >= day:
    if day % 11 == 0:
        quantity_decoration += 2

    if day % 2 == 0:
        budget += ornament_set * quantity_decoration
        spirit += 5

    if day % 3 == 0:
        budget += (tree_skirt + tree_garlands) * quantity_decoration
        spirit += 13

    if day % 5 == 0:
        budget += tree_lights * quantity_decoration
        spirit += 17

    if day % 15 == 0:

        spirit += 30

    if day % 10 == 0:
        spirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights


    day += 1

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")