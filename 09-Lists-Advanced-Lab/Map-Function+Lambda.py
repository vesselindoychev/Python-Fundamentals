#Map function converts list of strings into list of integers

nums_str = ["1", "2", "3", "4"]

my = list(map(lambda nums_str: int(nums_str), nums_str))
print(my)