rooms = int(input())

has_enough_chairs = True
free_chairs = 0
chairs_in_need = 0
for i in range(1, rooms + 1):
    chairs_per_room = input().split()
    chairs = chairs_per_room[0]
    people = int(chairs_per_room[1])

    if len(chairs) >= people:
        free_chairs += len(chairs) - people

    else:
        has_enough_chairs = False
        chairs_in_need += people - len(chairs)
        print(f"{chairs_in_need} more chairs needed in room {i}")

if has_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")