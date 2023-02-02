import sys
import math
students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

attendances = []
total_bonus = 0
for each_student in range(students_count):
    attendances_for_each_student = int(input())
    attendances.append(attendances_for_each_student)

max_attendances = 0
for i in attendances:
    max_attendances = max(attendances)

    total_bonus = max_attendances / lectures_count * (5 + initial_bonus)

print(f"Max Bonus: {math.ceil(total_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")