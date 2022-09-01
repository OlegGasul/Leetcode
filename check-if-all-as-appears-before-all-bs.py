def checkString(s: str) -> bool:
    a = False
    b = False
        
    for ch in s:
        if ch == "a":
            if b:
                return False
            a = True
        elif ch == "b":
            b = True
                
    return True

print(checkString("aaabbb"))
print(checkString("abab"))