first_employee_people = int(input())
second_employee_people = int(input())
third_employee_people = int(input())
total_people_count = int(input())

hour = 0
helped_people_per_hour = first_employee_people + second_employee_people + third_employee_people
while total_people_count > 0:
    total_people_count -= helped_people_per_hour
    hour += 1

    if hour % 4 == 0:
        hour += 1

    if total_people_count == 0:
        break
print(f"Time needed: {hour}h.")

