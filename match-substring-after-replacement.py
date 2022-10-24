from collections import defaultdict

def matchReplacement(s: str, sub: str, mappings) -> bool:
    swaps = defaultdict(set)

    for f, t in mappings:
        swaps[f].add(t)

    dp = []

    for ch in sub:
        swaps[ch].add(ch)
        dp.append(swaps[ch])

    for i in range(len(s) - len(sub) + 1):
        if not s[i] in dp[0]:
            continue

        found = True
        for j in range(1, len(dp)):
            if not s[i + j] in dp[j]:
                found = False
                break

        if found:
            return True

    return False


print(matchReplacement("fool3e7bar", "leet", [["e", "3"], ["t", "7"], ["t", "8"]]))
print(matchReplacement("fooleetbar", "f00l", [["o", "0"]]))
print(matchReplacement("Fool33tbaR", "leetd", [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]]))