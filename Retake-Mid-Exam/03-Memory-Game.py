elements = input().split()

while True:
    command = input()

    tokens = command.split()



    if command == "end":
        break
    else:
        first_index = tokens[0]
        second_index = tokens[1]
for element in elements:
    if first_index == element or second_index == element:
        elements.remove(element)

print(elements)
