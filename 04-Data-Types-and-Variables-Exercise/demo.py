lost_fights_number = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0

budget = 0
for lose in range(1, lost_fights_number + 1):
    if lose % 2 == 0:
        broken_helmet += 1
        budget += helmet_price

    if lose % 3 == 0:
        broken_sword += 1
        budget += sword_price

    if lose % 6 == 0:
        broken_shield += 1
        budget += shield_price

        if broken_shield == 2:
            broken_armor += 1
            budget += armor_price
            broken_shield = 0

print(f"Gladiator expenses: {budget:.2f} aureus")
