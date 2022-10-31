def mergeAlternately(word1: str, word2: str) -> str:
    word1 = list(word1)
    word2 = list(word2)
        
    result = []
        
    while word1 or word2:
        if word1:
            result.append(word1.pop(0))
        
        if word2:
            result.append(word2.pop(0))
                
    return ''.join(result)

print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))