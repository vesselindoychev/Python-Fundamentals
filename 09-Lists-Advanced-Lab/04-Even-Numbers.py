# 1)FOR LOOP
nums_str = input().split(", ")

even_indices = []
numbers = []
for num_str in nums_str:
    number = int(num_str)
    numbers.append(number)

for index, number in enumerate(numbers):
    if number % 2 == 0:
        even_indices.append(index)

print(even_indices)

# 2)MAP
numbers = map(int, input().split(", "))
print([index for index, number in enumerate(numbers) if number % 2 == 0])
