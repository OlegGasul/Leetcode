def numSplits(s: str) -> int:
    length = len(s)
    
    dp = [0] * length
    chars = set()

    for i in range(length):
        chars.add(s[i])
        dp[i] = len(chars)

    dp2 = [0] * length
    chars = set()

    for i in reversed(range(length)):
        chars.add(s[i])
        dp2[i] = len(chars)

    result = 0
    for i in range(length - 1):
        if dp[i] == dp2[i + 1]:
            result += 1

    return result


print(numSplits("aacaba"))
print(numSplits("abcd"))