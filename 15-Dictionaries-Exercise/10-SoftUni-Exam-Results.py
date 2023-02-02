result = {}
submissions = {}
res_language = {}
res_points = {}
while True:
    command = input()
    if command == "exam finished":
        break

    tokens = command.split('-')
    username = tokens[0]
    if command == f'{username}-banned':
        result.pop(username)
        continue
    language = tokens[1]
    points = tokens[2]

    if username not in res_language:
        res_language[username] = []
        res_points[username] = []
    res_language[username].append(language)
    res_points[username].append(points)

    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1
    for name, points in res_points.items():
        result[name] = int(max(points))

sorted_results = sorted(result.items(), key=lambda kvp: (-kvp[1], kvp[0]))
sorted_submissions = sorted(submissions.items(), key=lambda kvp2: (-kvp2[1], kvp2[0]))

print('Results:')
for key, (value) in sorted_results:
    print(f"{key} | {value}")
print('Submissions:')
for key2, value2 in sorted_submissions:
    print(f"{key2} - {value2}")
