def canBeTypedWords(text: str, brokenLetters: str) -> int:
    words = text.split(' ')
        
    if len(brokenLetters) == 0:
        return len(words)
        
    result = 0
        
    brokenLetters = set(brokenLetters)
        
    for word in words:
        if len(set(word).intersection(brokenLetters)) == 0:
            result += 1
                
    return result

print(canBeTypedWords("hello world", "ad"))
print(canBeTypedWords("leet code", "lt"))