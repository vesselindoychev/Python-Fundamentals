words = input().split(", ")
text = input()

res = []

for word in words:
    if word in text:
        res.append(word)
print(res)

# COMPREHENSION
# words = input().split(", ")
# text = input()
#
# res = [word for word in words if word in text]
# print(res)