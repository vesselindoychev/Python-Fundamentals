numbers = list(map(int, input().split(", ")))

for number in numbers:
    if number == 0:
        numbers.remove(0)
        numbers.append(0)

print(numbers)
