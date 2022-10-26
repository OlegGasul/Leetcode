def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    a = ord('a')
        
    def sumWord(word):
        total = 0
            
        for ch in word:
            total *= 10
            total += ord(ch) - a
                
        return total
    
    return sumWord(targetWord) == sumWord(firstWord) + sumWord(secondWord)

print(isSumEqual("acb", "cba", "cdb"))
print(isSumEqual("aaa", "a", "aab"))