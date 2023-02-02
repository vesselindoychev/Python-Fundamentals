numbers = list(map(int, input().split()))
position = int(input())

result = []
counter = 0

index = 0
while len(numbers) > 0:
    counter += 1
    if counter % position == 0:
        result.append(numbers.pop(index))
    else:
        index += 1

    if index >= len(numbers):
        index = 0

str_numbers = ",".join(list(map(str, result)))
print(f"[{str_numbers}]")
