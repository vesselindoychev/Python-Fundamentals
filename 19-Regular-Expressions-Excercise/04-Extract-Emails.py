import re

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\.\-\_]?[a-zA-Z0-9]+@[a-z]+\-?[a-z]+(\.[a-z]+)+"

match_mails = [obj.group() for obj in re.finditer(pattern, text)]
print("\n".join(match_mails))