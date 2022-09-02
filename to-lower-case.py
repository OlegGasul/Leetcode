def toLowerCase(s: str) -> str:
    letters = list(s)
    a = ord('a')
        
    for i in range(len(letters)):
        value = ord(letters[i])
        if value >= 65 and value <= 90:
            value = a + value - 65
            letters[i] = chr(value)
                
    return ''.join(letters)

print(toLowerCase("Hello"))
print(toLowerCase("LOVELY"))
print(toLowerCase("here"))