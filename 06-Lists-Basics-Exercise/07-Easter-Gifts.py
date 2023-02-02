gifts = input().split()
gifts_out_of_stoke = 0
while True:
    command = input()
    if command == "No Money":
        break

    tokens = command.split()
    command = tokens[0]

    if command == "OutOfStock":
        gifts_out_of_stoke = tokens[1]

        for i in gifts:
            if i == gifts_out_of_stoke:
                gifts[gifts.index(i)] = "None"

    elif command == "Required":
        gift_replacement = tokens[1]
        index = int(tokens[2])

        if 0 <= index <= len(gifts):
            gifts[index] = gift_replacement
        else:
            continue

    elif command == "JustInCase":
        just_in_case_gift = tokens[1]
        gifts[len(gifts) - 1] = just_in_case_gift

for i in gifts:
    if i != "None":
        print(i, end=" ")