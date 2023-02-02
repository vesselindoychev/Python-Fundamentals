command = input()

corresponding_side = {}
corresponding_force_side = {}
while not command == "Lumpawaroo":
    if '|' in command:
        tokens = command.split(' | ')
        force_side = tokens[0]
        force_user = tokens[1]

        if force_side not in corresponding_side:
            corresponding_side[force_side] = []


        if force_user not in corresponding_side[force_side]:
            corresponding_side[force_side].append(force_user)
        # if force_user in corresponding_side[force_side]:
            # corresponding_side[force_side].append(force_user)
            # corresponding_side[force_side].remove(force_user)


    elif '->' in command:
        tokens = command.split(' -> ')
        force_user = tokens[0]
        force_side = tokens[1]

        for key, value in corresponding_side.items():
            if force_user in value:
                value.remove(force_user)
        if force_side not in corresponding_side:
            corresponding_side[force_side] = []
        if force_user not in corresponding_side[force_side]:
            corresponding_side[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        # if force_user in corresponding_side[force_side]:
        #     corresponding_side.pop(force_user)
            # corresponding_force_side[force_side] = []
            # corresponding_force_side[force_side].append(force_user)
            #

    command = input()

sorted_sides = sorted(corresponding_side.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

for side, user in sorted_sides:
    if len(user) > 0:
        print(f"Side: {side}, Members: {len(user)}")

        for name in sorted(user):
            print(f"! {name}")