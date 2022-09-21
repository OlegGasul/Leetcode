def freqAlphabets(s: str) -> str:
    a = ord('a') - 1
    i = len(s) - 1
        
    result = ""
        
    while i >= 0:
        if s[i] == "#":
            result = chr(a + int(s[i - 2 : i])) + result
            i -= 3
        else:
            result = chr(a + int(s[i])) + result
            i -= 1
                
    return result

print(freqAlphabets("10#11#12"))
print(freqAlphabets("1326#"))