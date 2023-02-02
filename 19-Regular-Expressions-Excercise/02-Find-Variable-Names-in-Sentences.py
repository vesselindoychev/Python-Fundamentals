import re

text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

valid_vars = [obj.group() for obj in re.finditer(pattern, text)]

print(*valid_vars, sep=",")