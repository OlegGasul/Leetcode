def countPrefixes(words, s: str) -> int:
    result = 0
        
    for word in words:
        if len(word) > len(s):
            continue
                
        equal = True
        for i in range(len(word)):
            if word[i] != s[i]:
                equal = False
                break
                    
        if equal:
            result += 1
                
    return result

print(countPrefixes(["a", "b", "c", "ab", "bc", "abc"], "abc"))