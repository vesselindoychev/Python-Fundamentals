def is_perfect_number(number):
    res = []
    for i in range(1, number + 1):
        if number % i == 0:
            res.append(i)

    res.remove(res[-1])

    if sum(res) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

is_perfect_number(number)
