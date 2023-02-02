import re

text = input()
all_sites = []
pattern = r"w{3}\.[a-zA-Z0-9]+(\-?[a-zA-Z0-9])+(\.[a-z]+)+"
while not text == "":
    valid_sites = [obj.group() for obj in re.finditer(pattern, text)]

    all_sites.extend(valid_sites)

    text = input()

print("\n".join(all_sites))



