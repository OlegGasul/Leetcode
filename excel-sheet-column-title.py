def convertToTitle(columnNumber: int) -> str:
    if columnNumber < 1:
        return ""
    
    letters = 26
    a = ord("A")

    result = []

    while columnNumber > 0:
        columnNumber -= 1
        result.append(chr(a + columnNumber % letters))
        columnNumber //= letters

    return ''.join(reversed(result))
        

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))
print(convertToTitle(1171111101))