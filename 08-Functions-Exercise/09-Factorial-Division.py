def factorial_division(first_number, second_number):
    factorial_sum_one = 1
    factorial_sum_two = 1

    for factorial_one in range(1, first_number + 1):
        factorial_sum_one *= factorial_one

    for factorial_two in range(1, second_number + 1):
        factorial_sum_two *= factorial_two

    result = factorial_sum_one // factorial_sum_two
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
