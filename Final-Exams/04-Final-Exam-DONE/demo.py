n = int(input())

adventure_game = {}
for _ in range(n):
    string = input().split()
    hero_name = string[0]
    hp = int(string[1])
    mana = int(string[2])

    if hero_name not in adventure_game:
        adventure_game[hero_name] = {"hp": hp, "mana": mana}

text = input()
while not text == "End":
    tokens = text.split(" - ")
    command = tokens[0]
    initial_hero = tokens[1]

    if command == "CastSpell":
        mana_needed = int(tokens[2])
        spell_name = tokens[3]

        if adventure_game[initial_hero]["mana"] >= mana_needed:
            adventure_game[initial_hero]["mana"] -= mana_needed
            print(f"{initial_hero} has successfully cast {spell_name} and "
                  f"now has {adventure_game[initial_hero]['mana']} MP!")
        else:
            print(f"{initial_hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        dmg = int(tokens[2])
        enemy = tokens[3]

        if adventure_game[initial_hero]["hp"] - dmg > 0:
            adventure_game[initial_hero]["hp"] -= dmg
            print(f"{initial_hero} was hit for {dmg} HP by {enemy}"
                  f" and now has {adventure_game[initial_hero]['hp']} HP left!")
        else:
            adventure_game.pop(initial_hero)
            print(f"{initial_hero} has been killed by {enemy}!")

    elif command == "Recharge":
        amount = int(tokens[2])
        recharged_mana = 0
        if adventure_game[initial_hero]["mana"] + amount > 200:
            recharged_mana = 200 - adventure_game[initial_hero]["mana"]
            adventure_game[initial_hero]["mana"] = 200
            print(f"{initial_hero} recharged for {recharged_mana} MP!")
        else:
            adventure_game[initial_hero]["mana"] += amount
            print(f"{initial_hero} recharged for {amount} MP!")

    elif command == "Heal":
        amount_hp = int(tokens[2])
        healed_hp = 0

        if adventure_game[initial_hero]["hp"] + amount_hp > 100:
            healed_hp = 100 - adventure_game[initial_hero]["hp"]
            adventure_game[initial_hero]["hp"] = 100
            print(f"{initial_hero} healed for {healed_hp} HP!")
        else:
            adventure_game[initial_hero]["hp"] += amount_hp
            print(f"{initial_hero} healed for {amount_hp} HP!")

    text = input()

sorted_heroes = sorted(adventure_game.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0]))

for key, value in sorted_heroes:
    print(f"{key}\n  HP: {value['hp']}\n  MP: {value['mana']}")