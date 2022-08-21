def checkCounts(letters, current):
    if len(current.keys()) != len(letters.keys()):
        return False

    for letter, count in current.items():
        if not letter in letters:
            return False

        if count != letters[letter]:
            return False

    return True
    

def findAnagrams(s: str, p: str):
    pLen = len(p)
    if pLen > len(s):
        return []

    letters = {}
    for x in p:
        if not x in letters:
            letters[x] = 0
        letters[x] += 1

    current = {}
    for position in range(pLen):
        letter = s[position]
        if not letter in current:
            current[letter] = 0
        current[letter] += 1
    
    result = []

    if checkCounts(letters, current):
        result.append(0)

    for i in range(position + 1, len(s)):
        first = s[i - pLen]

        current[first] -= 1
        if current[first] == 0:
            del current[first]
        
        letter = s[i]
        if not letter in current:
            current[letter] = 0
        current[letter] += 1
        
        if checkCounts(letters, current):
            result.append(i - pLen + 1)

    return result


print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))