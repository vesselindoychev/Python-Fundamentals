cards = input().split()

team_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

team_a_counter = 11
team_b_counter = 11

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    number = int(tokens[1])
    index = number - 1

    if team == "A":
        if team_a[index] == 0:
            continue
        team_a[index] = 0
        team_a_counter -= 1

    else:
        if team_b[index] == 0:
            continue
        team_b[index] = 0
        team_b_counter -= 1

    if team_a_counter < 7 or team_b_counter < 7:
        break

print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")

if team_a_counter < 7 or team_b_counter < 7:
    print("Game was terminated")
