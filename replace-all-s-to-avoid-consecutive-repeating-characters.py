import string

def modifyString(s: str) -> str:
    letters = set(string.ascii_lowercase)
    chars = list(s)
        
    for i in range(len(chars)):
        if chars[i] == "?":
            d = set()
            if i > 0:
                d.add(chars[i - 1])
            if i < len(s) - 1:
                d.add(chars[i + 1])
                    
            chars[i] = list(letters - d)[0]
                
    return ''.join(chars)

print(modifyString("?zs"))
print(modifyString("ubv?w"))