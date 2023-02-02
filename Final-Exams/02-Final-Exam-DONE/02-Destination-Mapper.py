import re

text = input()
pattern = r"(?<=(=|/))[A-Z][a-zA-Z]{2,}(?=\1)"
total_points = 0

valid_items = [obj.group() for obj in re.finditer(pattern, text)]

for item in valid_items:
    total_points += len(item)

print(f"Destinations: {', '.join(valid_items)}")
print(f"Travel Points: {total_points}")