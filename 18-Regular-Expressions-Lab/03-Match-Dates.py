import re

text = input()
pattern = r"\b(?P<Day>\d{2})(?P<separator>[\.\-\/])(?P<Month>[A-Z]{1}[a-z]{2})(?P=separator)(?P<Year>\d{4})\b"

valid_dates = [obj.groupdict() for obj in re.finditer(pattern, text)]


for data in valid_dates:
    print(f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}")
