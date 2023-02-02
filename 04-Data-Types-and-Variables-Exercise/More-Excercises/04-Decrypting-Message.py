key = int(input())
symbols = int(input())

secret_message = []

for i in range(symbols):
    symbol = input()

    value = ord(symbol) + key

    secret_message.append(chr(value))


print("".join(secret_message))