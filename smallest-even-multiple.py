def smallestEvenMultiple(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        return 2 * n

print(smallestEvenMultiple(5))
print(smallestEvenMultiple(6))