numbers = list(map(int, input().split()))

biggest_nums = []
total_sum = 0
for number in numbers:
    total_sum += number

if total_sum // len(numbers) == number:
    print("No")


for number in numbers:
    if total_sum // len(numbers) < number:
        biggest_nums.append(number)
biggest_nums.sort()
biggest_nums = biggest_nums[-5:]
biggest_nums.reverse()



numbers = biggest_nums

text = []
for i in numbers:
    str_num = str(i)
    text.append(str_num)
print(" ".join(text))