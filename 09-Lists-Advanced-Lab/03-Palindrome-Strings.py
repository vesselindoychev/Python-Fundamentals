is_palindrome = lambda word: word == word[::-1]

words = input().split()
searched_word = input()
palindromes = [word for word in words if is_palindrome(word)]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_word)} times")
