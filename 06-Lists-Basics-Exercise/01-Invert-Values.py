string = input().split()
numbers = []

for num_str in string:
    number = -int(num_str)
    numbers.append(number)
print(numbers)