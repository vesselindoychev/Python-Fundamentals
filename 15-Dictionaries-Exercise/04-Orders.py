command = input()

products = {}
while not command == 'buy':

    tokens = command.split()

    name = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])

    if name not in products:
        products[name] = []
        products[name].append(price)
        products[name].append(quantity)
    else:
        products[name][0] = price
        products[name][1] += quantity
    command = input()

for name, products[name] in products.items():

    print(f"{name} -> {products[name][0] * products[name][1]:.2f}")