def removeStars(s: str) -> str:
    letters = []
        
    for i in range(len(s)):
        if s[i] == "*":
            letters.pop()
        else:
            letters.append(s[i])
            
    return ''.join(letters)

print(removeStars("leet**cod*e"))