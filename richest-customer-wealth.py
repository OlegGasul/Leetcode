def maximumWealth(accounts) -> int:
    if len(accounts) == 0:
        return 0
    return max([sum(x) for x in accounts])

print(maximumWealth([[1, 2, 3], [3, 2, 1]]))
print(maximumWealth([[], []]))
print(maximumWealth([]))