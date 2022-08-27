def largeGroupPositions(s: str):
    length = len(s)
    if length < 3:
        return []

    result = []

    start = 0
    for i in range(length):
        if s[i] != s[i - 1]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i

    if length - start >= 3:
        result.append([start, length - 1])

    return result

print(largeGroupPositions("abbxxxxzzy"))
print(largeGroupPositions("aaabbxxxxzzyyy"))
print(largeGroupPositions("abcdefgh"))