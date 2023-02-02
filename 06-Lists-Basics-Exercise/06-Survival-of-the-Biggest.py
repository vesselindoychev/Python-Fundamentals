nums_str = input().split()
n = int(input())

numbers = []
for num_str in nums_str:
    number = int(num_str)
    numbers.append(number)


for i in range(n):
    numbers.remove(min(numbers))
print(numbers)