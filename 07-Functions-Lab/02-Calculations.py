def operation_numbers(firts_num, second_num, operator):
    result = 0
    if operator == "multiply":
        result = firts_num * second_num

    if operator == "divide":
        result = int(firts_num / second_num)

    if operator == "add":
        result = firts_num + second_num

    if operator == "subtract":
        result = firts_num - second_num

    return result


operator = input()
first_num = int(input())
second_num = int(input())

print(operation_numbers(first_num, second_num, operator))