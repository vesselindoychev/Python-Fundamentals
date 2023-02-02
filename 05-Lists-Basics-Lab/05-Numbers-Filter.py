n = int(input())

numbers = []
filtered = []

for num in range(1, n + 1):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
    print(filtered)

if command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
    print(filtered)

if command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)
    print(filtered)

if command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
    print(filtered)