from collections import Counter

def countCharacters(words, chars: str) -> int:
    chars = Counter(chars)
        
    result = 0
        
    for word in words:
        length = len(word)
        word = Counter(word)
            
        if chars & word == word:
            result += length
                
    return result

print(countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print(countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))