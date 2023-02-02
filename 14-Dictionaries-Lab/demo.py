text = input().split()

obtained_items = {"shards": "Shadowmourne", "motes": "Dragonwrath", "fragments": "Valanyr"}
key_materials = {"shards": 0, "motes": 0, "fragments": 0}
junk_materials = {}
is_obtained = False
while True:
    if is_obtained:
        break
    for index in range(0, len(text), 2):
        if is_obtained:
            break
        quantity = int(text[index])
        item_name = text[index + 1].lower()

        if item_name in key_materials:
            key_materials[item_name] += quantity

        else:
            if item_name not in junk_materials:
                junk_materials[item_name] = quantity
            else:
                junk_materials[item_name] += quantity

        for item_name, count in key_materials.items():
            if count >= 250:
                key_materials[item_name] -= 250
                for name, obtained_item in obtained_items.items():
                    print(f"{obtained_items[item_name]} obtained!")
                    is_obtained = True
                    break


sorted_key_items = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_junk_items = sorted(junk_materials.items(), key=lambda kvp2: kvp2[0])

for name, count in sorted_key_items:
    print(f"{name}: {count}")

for name2, count2 in sorted_junk_items:
    print(f"{name2}: {count2}")
