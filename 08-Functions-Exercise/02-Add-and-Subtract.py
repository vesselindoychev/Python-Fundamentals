def sum_numbers(first_number, second_number):
    result = first_number + second_number
    return result


def subtract_numbers(first_number, second_number):
    return first_number - second_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

sum = sum_numbers(first_number, second_number)
result = subtract_numbers(sum, third_number)
print(result)
