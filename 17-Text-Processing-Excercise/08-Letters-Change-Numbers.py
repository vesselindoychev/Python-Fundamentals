import string

words = input().split()
total_sum = 0
sum_of_res = 0
res = 0
first_pos_upper_letter = ''
first_pos_lower_letter = ''
last_pos_upper_letter = ''
last_pos_lower_letter = ''
letters = []
for word in words:
    current_number = ''
    letters = []
    for index in range(len(word)):
        if word[index].isdigit():
            current_number += word[index]
        else:
            letters.append(word[index])
    current_number = int(current_number)
    if letters[0].isupper():
        first_pos_upper_letter = string.ascii_uppercase.index(letters[0])
        first_pos_upper_letter = int(first_pos_upper_letter) + 1
        res += current_number / first_pos_upper_letter

        first_pos_upper_letter = ''


    elif letters[0].islower():
        first_pos_lower_letter = string.ascii_lowercase.index(letters[0])
        first_pos_lower_letter = int(first_pos_lower_letter) + 1
        res += current_number * first_pos_lower_letter

        first_pos_lower_letter = ''

    if letters[1].isupper():
        last_pos_upper_letter = string.ascii_uppercase.index(letters[1])
        last_pos_upper_letter = int(last_pos_upper_letter) + 1
        res -= last_pos_upper_letter

        last_pos_upper_letter = ''

    elif letters[1].islower():
        last_pos_lower_letter = string.ascii_lowercase.index(letters[1])
        last_pos_lower_letter = int(last_pos_lower_letter) + 1
        res += last_pos_lower_letter

        last_pos_lower_letter = ''

print(f"{res:.2f}")
