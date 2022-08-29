import functools

def findLongestChain(pairs) -> int:
    def compare(a, b):
        return a[1] - b[1]

    pairs = sorted(pairs, key = functools.cmp_to_key(compare))
    print(pairs)

    current = float('-inf')
    result = 0

    for x, y in pairs:
        if current < x:
            current = y
            result += 1

    return result


print(findLongestChain([[1, 2], [2, 3], [4, 5], [7, 8], [4, 5], [3, 9]]))