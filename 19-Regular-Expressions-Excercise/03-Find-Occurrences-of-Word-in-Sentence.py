import re

text = input()
searched_word = input()

pattern = rf"\b{searched_word}\b"
count_words = re.findall(pattern, text, re.IGNORECASE)
print(len(count_words))