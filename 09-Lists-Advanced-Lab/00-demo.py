str_nums = input().split(", ")

nums = list(map(int, str_nums))

new_n = list(filter(lambda x: x % 2 == 0, nums))

print(new_n)