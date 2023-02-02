commands = input()

social_media = {}
while not commands == "Log out":
    tokens = commands.split(": ")
    command = tokens[0]
    username = tokens[1]
    if command == "New follower":
        if username not in social_media:
            social_media[username] = {"likes": 0, "comments": 0}


    elif command == "Like":
        count = int(tokens[2])

        if username not in social_media:
            social_media[username] = {"likes": count, "comments": 0}
        else:
            social_media[username]["likes"] += count

    elif command == "Comment":
        if username not in social_media:
            social_media[username] = {"likes": 0, "comments": 1}
        else:
            social_media[username]["comments"] += 1

    elif command == "Blocked":
        if username in social_media:
            social_media.pop(username)
        else:
            print(f"{username} doesn't exist.")

    commands = input()

records = {}

for key, value in social_media.items():
    sum_of_value = value["likes"] + value["comments"]
    if key not in records:
        records[key] = sum_of_value

sorted_records = sorted(records.items(), key=lambda kvp: (-kvp[1], kvp[0]))

print(f"{len(sorted_records)} followers")
for name, record in sorted_records:
    print(f"{name}: {record}")