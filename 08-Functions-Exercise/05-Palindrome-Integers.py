def palindrome_integers(numbers_str):
    for num_str in numbers_str:
        if num_str == num_str[::-1]:
            print("True")
        else:
            print("False")


numbers_str = input().split(", ")
palindrome_integers(numbers_str)
