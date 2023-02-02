def odd_and_even_sum(number_str):
    even = 0
    odd = 0
    for index in number_str:
        num = int(index)
        if num % 2 == 0:
            even += num
        else:
            odd += num

    return f"Odd sum = {odd}, Even sum = {even}"


number_str = input()
print(odd_and_even_sum(number_str))