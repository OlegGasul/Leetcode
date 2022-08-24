def distributeCandies(candyType) -> int:
    return len(list(set(candyType))[0 : len(candyType) // 2])

print(distributeCandies([1, 1, 2, 3]))
print(distributeCandies([1, 1, 2, 3, 2, 2, 3, 3, 4]))