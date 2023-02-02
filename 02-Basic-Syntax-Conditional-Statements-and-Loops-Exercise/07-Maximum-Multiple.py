divisor = int(input())
bound = int(input())

n = bound

while True:
    if n % divisor == 0 and 0 < n <= bound:
        print(n)
        break
    else:
        n -= 1