def cellsInRange(s: str):
    fromLetter, fromDigit, sep, toLetter, toDigit = s
        
    fromLetter = ord(fromLetter)
    fromDigit = int(fromDigit)
        
    toLetter = ord(toLetter)
    toDigit = int(toDigit)
        
    result = []
        
    while fromLetter <= toLetter:
        i = fromDigit
        letter = chr(fromLetter)
            
        while i <= toDigit:
            result.append(letter + str(i))
            i += 1
            
        fromLetter += 1
            
    return result

print(cellsInRange("K1:L2"))
print(cellsInRange("A1:F1"))