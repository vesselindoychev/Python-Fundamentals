n = int(input())

hero_data = {}
for _ in range(n):
    data = input().split()
    hero_name = data[0]
    hp = int(data[1])
    mana = int(data[2])
    if hero_name not in hero_data:
        hero_data[hero_name] = {"hp": hp, "mana": mana}

text = input()
while not text == "End":

    tokens = text.split(" - ")
    command = tokens[0]
    initial_hero = tokens[1]

    if command == "CastSpell":
        mana_needed = int(tokens[2])
        spell_name = tokens[3]

        if hero_data[initial_hero]["mana"] >= mana_needed:
            hero_data[initial_hero]["mana"] -= mana_needed
            print(f"{initial_hero} has successfully cast {spell_name} "
                  f"and now has {hero_data[initial_hero]['mana']} MP!")
        else:
            print(f"{initial_hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(tokens[2])
        enemy = tokens[3]

        if hero_data[initial_hero]["hp"] - damage > 0:
            hero_data[initial_hero]["hp"] -= damage
            print(f"{initial_hero} was hit for {damage} HP by {enemy} and now has"
                  f" {hero_data[initial_hero]['hp']} HP left!")
        else:
            hero_data.pop(initial_hero)
            print(f"{initial_hero} has been killed by {enemy}!")

    elif command == "Recharge":
        amount_mana = int(tokens[2])
        reg_mana = 0
        if hero_data[initial_hero]["mana"] + amount_mana >= 200:
            reg_mana = 200 - hero_data[initial_hero]["mana"]
            hero_data[initial_hero]["mana"] = 200
            print(f"{initial_hero} recharged for {reg_mana} MP!")

        else:
            hero_data[initial_hero]["mana"] += amount_mana
            reg_mana = amount_mana
            print(f"{initial_hero} recharged for {reg_mana} MP!")

    elif command == "Heal":
        amount_hp = int(tokens[2])
        reg_hp = 0

        if hero_data[initial_hero]["hp"] + amount_hp >= 100:
            reg_hp = 100 - hero_data[initial_hero]["hp"]
            hero_data[initial_hero]["hp"] = 100
            print(f"{initial_hero} healed for {reg_hp} HP!")
        else:
            hero_data[initial_hero]["hp"] += amount_hp
            reg_hp = amount_hp
            print(f"{initial_hero} healed for {reg_hp} HP!")

    text = input()

sorted_data = sorted(hero_data.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0]))

for key, value in sorted_data:
    print(f"{key}\n  HP: {value['hp']}\n  MP: {value['mana']}")
