products = input().split()
searched_products = input().split()

food = {}
for i in range(0, len(products), 2):
    product_name = products[i]
    product_quantity = products[i + 1]
    food[product_name] = int(product_quantity)
for element in searched_products:
    if element in food:
        print(f"We have {food[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")
