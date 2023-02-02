number = int(input())

for special_num in range(1, number + 1):

    sum_of_digits = 0

    for digit in str(special_num):
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{special_num} -> True")
    else:
        print(f"{special_num} -> False")



