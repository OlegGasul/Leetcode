def detectCapitalUse(word: str) -> bool:
    length = len(word)
    if length == 0:
        return True
        
    allUppers = True
    allLowers = True
    firstUpper = word[0].isupper()
        
    for i in range(1, length):
        if word[i].islower():
            allUppers = False
        elif word[i].isupper():
            allLowers = False
                
    return (firstUpper and allUppers) or (firstUpper and allLowers) or (not firstUpper and allLowers)

print(detectCapitalUse("USA"))
print(detectCapitalUse("FlaG"))