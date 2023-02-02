number = input()
num = 0
nums = []
for i in range(len(number)):
    nums.append(int(number[i]))

nums.sort(reverse=True)
new_str = []
for j in nums:
    num = str(j)
    new_str.append(num)
print("".join(new_str))