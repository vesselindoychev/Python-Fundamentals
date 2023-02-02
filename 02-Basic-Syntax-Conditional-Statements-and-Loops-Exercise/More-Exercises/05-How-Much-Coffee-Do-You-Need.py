command = input()
coffee = 0

while not command == "END":
    if command == "coding" or command == "movie" or command == "dog" or command == "cat":
        coffee += 1

    if command == "CODING" or command == "MOVIE" or command == "DOG" or command == "CAT":
        coffee += 2

    command = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)