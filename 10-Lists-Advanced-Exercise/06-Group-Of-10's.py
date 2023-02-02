import math
nums_str = input().split(", ")

numbers = list(map(lambda num: int(num), nums_str))

max_number = max(numbers)
number_of_groups = math.ceil(max_number / 10)

for i in range(1, number_of_groups + 1):

    upper_range = i * 10
    lower_range = upper_range - 10

    current_range = [num for num in numbers if upper_range >= num > lower_range]
    # current_range = []
    #
    # for num in numbers:
    #     upper_range = i * 10
    #     lower_range = upper_range - 10
    #
    #     if upper_range >= num > lower_range:
    #         current_range.append(num)
    print(f"Group of {i * 10}'s: {current_range}")