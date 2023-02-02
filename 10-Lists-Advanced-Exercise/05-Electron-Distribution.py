total_electrons = int(input())

index = 1
result = []

while total_electrons > 0:
    value = 2 * index ** 2

    if total_electrons > value:
        result.append(value)
    else:
        result.append(total_electrons)
    index += 1
    total_electrons -= value
print(result)