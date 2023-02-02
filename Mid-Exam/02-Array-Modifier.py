numbers = list(map(int, input().split()))

while True:
    arg = input()
    if arg == "end":
        break
    tokens = arg.split()
    command = tokens[0]
    if command == "decrease":
        decrease_func = [n - 1 for n in numbers]
        numbers = decrease_func
    # index_one = int(tokens[1])
    # index_two = int(tokens[2])
    else:
        index_one = int(tokens[1])
        index_two = int(tokens[2])
        if command == "swap":
            numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]

        elif command == "multiply":
            numbers[index_one] = numbers[index_one] * numbers[index_two]

strings = []

for i in numbers:
    num_str = str(i)
    strings.append(num_str)

print(", ".join(strings))



