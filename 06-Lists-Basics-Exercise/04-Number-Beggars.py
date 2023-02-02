nums_str = input().split(", ")
beggars_number = int(input())

numbers = []

for num_str in nums_str:
    number = int(num_str)
    numbers.append(number)

beggars = []
for i in range(beggars_number):
    beggars.append(0)

index = 0
#1, 2, 3, 4, 5
#2
for number in numbers:
    beggars[index] += number
    index += 1

    if index == beggars_number:
        index = 0

print(beggars)