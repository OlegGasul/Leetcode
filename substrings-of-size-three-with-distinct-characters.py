def countGoodSubstrings(s: str) -> int:
    if len(s) < 3:
        return 0
        
    letters = []
    length = 3
        
    for i in range(length):
        letters.append(s[i])

    result = 0
    
    if len(letters) == len(set(letters)):
        result += 1
    
    for j in range(i + 1, len(s)):
        letters.pop(0)
        letters.append(s[j])
        
        if len(letters) == len(set(letters)):
            result += 1
                
    return result

# print(countGoodSubstrings("xyzzaz"))
# print(countGoodSubstrings("aababcabc"))
print(countGoodSubstrings("npdrlvffzefb"))