data = input()

is_obtained = False
junk_materials = {}
obtained_materials = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
key_items = {'shards': 0, 'fragments': 0, 'motes': 0}
while not is_obtained:

    tokens = data.split()

    for index in range(0, len(tokens), 2):
        if is_obtained:
            break
        quantity = int(tokens[index])
        material = tokens[index + 1].lower()

        if material in key_items:
            key_items[material] += quantity

        else:
            if material not in junk_materials:
                junk_materials[material] = quantity
            else:
                junk_materials[material] += quantity

        for key, value in key_items.items():
            if value >= 250:
                is_obtained = True
                print(f"{obtained_materials[key]} obtained!")
                key_items[key] -= 250
                break
    if is_obtained:
        break
    data = input()

sorted_items = sorted(key_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

for name, qnt in sorted_items:
    print(f"{name}: {qnt}")

sorted_junks = sorted(junk_materials.items(), key=lambda kvp2: kvp2[0])

for name_junk, junk_quant in sorted_junks:
    print(f"{name_junk}: {junk_quant}")