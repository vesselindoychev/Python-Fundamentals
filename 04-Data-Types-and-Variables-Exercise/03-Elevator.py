import math
number_of_people = int(input())
capacity_of_elevator = int(input())

courses = number_of_people / capacity_of_elevator
print(math.ceil(courses))