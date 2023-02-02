products = input().split()

food = {}

# # Dict comprehension
# food = {products[index]: products[index + 1]
#         for index in range(0, len(products), 2)}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    food[key] = int(value)



print(food)