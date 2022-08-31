def repeatedCharacter(s: str) -> str:
    letters = set()
        
    for ch in s:
        if ch in letters:
            return ch
        letters.add(ch)
            
    return ""

print(repeatedCharacter("abccbaacz"))
print(repeatedCharacter("abcdd"))