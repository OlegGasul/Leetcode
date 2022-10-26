def halvesAreAlike(s: str) -> bool:
    def isVowel(ch):
        return ch in set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
    vowels = 0
        
    halfLength = len(s) // 2
        
    for i in range(halfLength):
        if isVowel(s[i]):
            vowels += 1
        if isVowel(s[i + halfLength]):
            vowels -= 1
                
    return vowels == 0

print(halvesAreAlike("book"))
print(halvesAreAlike("textbook"))