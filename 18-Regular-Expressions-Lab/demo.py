import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_numbers = [obj.group() for obj in re.finditer(pattern, text)]
print(*valid_numbers)