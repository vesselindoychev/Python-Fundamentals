company_list = {}

filtered_id = {}
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split(' -> ')
    company_name = tokens[0]
    person_id = tokens[1]

    if company_name not in company_list:
        company_list[company_name] = []

        company_list[company_name].append(person_id)

    else:
        if person_id in company_list[company_name]:
            continue
        company_list[company_name].append(person_id)


sorted_list = sorted(company_list.items(), key=lambda kvp: kvp[0])

for key, value in sorted_list:
    print(f"{key}")

    for each_id in value:
        print(f"-- {each_id}")