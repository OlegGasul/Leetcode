def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    letters = {}
    for x in s:
        if not x in letters:
            letters[x] = 0
        letters[x] += 1

    
    for x in t:
        if not x in letters:
            return False
        letters[x] -= 1
        if letters[x] == 0:
            del letters[x]

    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))  