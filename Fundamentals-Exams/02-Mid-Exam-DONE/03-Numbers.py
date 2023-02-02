numbers = list(map(int, input().split()))


res = []
average_num = sum(numbers) / len(numbers)
for number in numbers:
    if number > average_num:
        res.append(number)
        res = sorted(res, reverse=True)
    if len(res) > 5:
        res.pop()

if average_num == number:
    print("No")
print(" ".join(list(map(str, res))))