elements = list(map(int, input().split()))

while True:
    words = input()

    if words == "end":
        break

    tokens = words.split()
    command = tokens[0]

    if command == "swap":
        index_one = int(tokens[1])
        index_two = int(tokens[2])

        elements[index_one], elements[index_two] = elements[index_two], elements[index_one]

    elif command == "multiply":
        multiply_index_one = int(tokens[1])
        multiply_index_two = int(tokens[2])

        result = elements[multiply_index_one] * elements[multiply_index_two]
        elements[multiply_index_one] = result

    elif command == "decrease":
        elements = [x - 1 for x in elements]

print(", ".join(list(map(str, elements))))

