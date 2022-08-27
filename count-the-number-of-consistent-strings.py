def countConsistentStrings(allowed: str, words) -> int:
    allowed = set(allowed)
    
    result = 0
    for word in words:
        if not (set(word) - allowed):
            result += 1

    return result


print(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
print(countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))