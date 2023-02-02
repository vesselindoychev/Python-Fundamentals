str_numbers = input().split()
factor = int(input())

numbers = list(map(int, str_numbers))

mapped_numbers = [x * factor for x in numbers if x >= 0]

filtration = sum(mapped_numbers)
average_length = filtration / len(mapped_numbers)


filtered_max_numbers = [j for j in mapped_numbers if j >= average_length]


if len(filtered_max_numbers) >= len(mapped_numbers) // 2:
    print(f"Score: {len(filtered_max_numbers)}/{len(mapped_numbers)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_max_numbers)}/{len(mapped_numbers)}. Employees are not happy!")

