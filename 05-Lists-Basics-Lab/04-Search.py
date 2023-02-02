n = int(input())
word = input()

word_list = []
new_word_list = []
for i in range(1, n + 1):
    text = input()

    word_list.append(text)

    if word in text:
        new_word_list.append(text)
print(word_list)
print(new_word_list)
