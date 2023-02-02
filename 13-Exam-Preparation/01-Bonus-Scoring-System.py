number_of_students = int(input())
number_of_lectures = int(input())
initial_bonus = int(input())

total_bonus = 0
attendences = []
max_attendences = 0

for each_student in range(number_of_students):
    count_of_attendences = int(input())
    attendences.append(count_of_attendences)

for i in attendences:
    max_attendences = max(attendences)

    total_bonus = max_attendences / number_of_lectures * (5 + initial_bonus)

print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_attendences} lectures.")