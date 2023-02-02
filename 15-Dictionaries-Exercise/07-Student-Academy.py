n = int(input())
average_grade = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in average_grade:

        average_grade[student_name] = []
        average_grade[student_name].append(grade)
    else:
        average_grade[student_name].append(grade)

filtered_grades = {}
for key, value in average_grade.items():
    res = sum(value) / len(value)
    if res >= 4.5:
        filtered_grades[key] = res

sorted_higher_res = dict(sorted(filtered_grades.items(), key=lambda kvp: kvp[1], reverse=True))

for name, avg_grd in sorted_higher_res.items():
    print(f"{name} -> {avg_grd:.2f}")