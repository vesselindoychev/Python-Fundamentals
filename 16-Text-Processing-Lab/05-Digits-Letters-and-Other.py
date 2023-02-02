word = input()

is_digit = []
is_symbol = []
is_char = []

for i in word:
    if i.isdigit():
        is_digit.append(i)

    elif i.isalpha():
        is_char.append(i)

    else:
        is_symbol.append(i)

print(''.join(is_digit))
print(''.join(is_char))
print(''.join(is_symbol))