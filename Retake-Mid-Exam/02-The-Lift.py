number_of_people = int(input())
current_state = input().split()



numbers = []
for num_str in current_state:
    number = int(num_str)
    numbers.append(number)

while number_of_people > 0:
    index = 0
    numbers[index] += 1
    number_of_people -= 1
    if numbers[index] == 4:
        numbers[index + 1] += 1

print(numbers)
print(number_of_people)


