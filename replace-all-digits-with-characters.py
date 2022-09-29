def replaceDigits(s: str) -> str:
    letters = list(s)
        
    for i in range(len(letters)):
        if i % 2 == 0:
            letter = letters[i]
        else:
            letters[i] = chr(ord(letter) + int(letters[i]))
                
    return ''.join(letters)

print(replaceDigits("a1c1e1"))
print(replaceDigits("a1b2c3d4e"))