text = input().split()

first_word = text[0]
second_word = text[1]

min_length = min(len(first_word), len(second_word))

total_sum = 0
for i in range(min_length):
    result = (ord(first_word[i]) * ord(second_word[i]))
    total_sum += result


bigger_word = first_word
if len(second_word) > len(first_word):
    bigger_word = second_word

for i in range(min_length, len(bigger_word)):
    total_sum += ord(bigger_word[i])

print(total_sum)

