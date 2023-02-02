price_ratings = list(map(int, input().split()))
entry_point = int(input())
type_of_items = input()

left_res = []
right_res = []
left_cheap = []
right_cheap = []

if type_of_items == "cheap":
    for i in range(0, entry_point):
        if price_ratings[i] < price_ratings[entry_point]:
            left_cheap.append(price_ratings[i])

    for x in range(entry_point + 1, len(price_ratings)):
        if price_ratings[x] < price_ratings[entry_point]:
            right_cheap.append(price_ratings[x])

    if sum(left_cheap) > sum(right_cheap):
        print(f"Left - {sum(left_cheap)}")
    elif sum(right_cheap) > sum(left_cheap):
        print(f"Right - {sum(right_cheap)}")
    else:
        print(f"Left - {sum(left_cheap)}")

elif type_of_items == "expensive":
    for j in range(0, entry_point):
        if price_ratings[j] >= price_ratings[entry_point]:
            left_res.append(price_ratings[j])

    for k in range(entry_point + 1, len(price_ratings)):
        if price_ratings[k] >= price_ratings[entry_point]:
            right_res.append(price_ratings[k])

    if sum(left_res) > sum(right_res):
        print(f"Left - {sum(left_res)}")
    elif sum(right_res) > sum(left_res):
        print(f"Right - {sum(right_res)}")
    else:
        print(f"Left - {sum(left_res)}")
