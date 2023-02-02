first_queue = int(input())
second_queue = int(input())
third_queue = int(input())
students_count = int(input())
time_needed = 0
while students_count >= 0:

    efficiency_per_hour = first_queue + second_queue + third_queue
    time_needed += 1
    students_count -= efficiency_per_hour

    if time_needed % 4 == 0:
        students_count += efficiency_per_hour

    if students_count == 0:
        break

print(f"Time needed: {time_needed}h.")
