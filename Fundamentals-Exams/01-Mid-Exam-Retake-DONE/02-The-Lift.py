people = int(input())
wagons = list(map(int, input().split()))
counter = 0
for index in range(len(wagons)):

    free_spot = 4 - wagons[index]

    if 0 <= wagons[index] < 4:
        if wagons[index] + people <= 4:
            wagons[index] += people
            people = 0
            break
        else:
            people -= 4 - wagons[index]
            wagons[index] += 4 - wagons[index]

if wagons.count(4) < len(wagons):
    print("The lift has empty spots!")
    print(" ".join(map(str, wagons)))

elif wagons.count(4) == len(wagons) and people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(map(str, wagons)))
else:
    print(" ".join(map(str, wagons)))
