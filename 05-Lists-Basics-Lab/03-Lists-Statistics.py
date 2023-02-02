n = int(input())

positives = []
negatives = []

for i in range(1, n + 1):
    numbers = int(input())

    if numbers > 0:
        positives.append(numbers)

    else:
        negatives.append(numbers)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")