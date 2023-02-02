text = input()

index = 0
current_string = ''
final_res = ''
while index < len(text):

    if not text[index].isdigit():
        current_string += text[index]
        index += 1
    else:
        current_number = ''
        while text[index].isdigit():
            current_number += text[index]
            index += 1

            if index == len(text):
                break
        current_number = int(current_number)
        output = current_number * current_string.upper()
        final_res += output
        output = ''
        current_string = ''
my_set = set(final_res)

print(f"Unique symbols used: {len(my_set)}")
print(final_res)