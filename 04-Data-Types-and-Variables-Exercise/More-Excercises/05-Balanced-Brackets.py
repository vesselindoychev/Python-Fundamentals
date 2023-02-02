lines = int(input())

balanced = True
last_symbol = ""
parentheses = []

for x in range(lines):
    symbol = input()

    if symbol == "(" and last_symbol == "(":
        balanced = False
        break
    parentheses.append(symbol)

    if symbol == "(" or symbol == ")":
        last_symbol = symbol

if parentheses.count("(") == parentheses.count(")"):
    print("BALANCED")
else:
    print("UNBALANCED")