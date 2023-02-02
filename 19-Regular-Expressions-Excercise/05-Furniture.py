import re

line = input()
pattern = r""
furniture_names = []
total_money = 0

while not line == "Purchase":
    match = re.match(pattern, line)