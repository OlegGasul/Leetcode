def maxPower(s: str) -> int:
    if not s:
        return 0
    
    length = len(s)
    
    result = 0
    counter = 0

    for i in range(1, length):
        if s[i] == s[i - 1]:
            counter += 1
        else:
            counter = 0

        result = max(result, counter)

    return result + 1

print(maxPower("leetcode"))
print(maxPower("abbcccddddeeeeedcba"))
print(maxPower(""))