n = int(input())

parking_list = {}

for i in range(n):
    text = input()
    tokens = text.split()

    command = tokens[0]
    name = tokens[1]

    if command == "register":
        license_plate_num = tokens[2]
        if name not in parking_list:
            parking_list[name] = license_plate_num
            print(f"{name} registered {license_plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_num}")
            continue

    elif command == "unregister":
        if name not in parking_list:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking_list.pop(name)


for key, value in parking_list.items():
    print(f"{key} => {value}")