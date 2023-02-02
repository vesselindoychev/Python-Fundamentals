# from _collections import defaultdict
#
# synonyms = defaultdict(list)

synonyms = {}
n = int(input())

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonyms in synonyms.items():
    normalized_synonyms = ", ".join(synonyms)
    print(f"{word} - {normalized_synonyms}")