def numSub(s: str) -> int:
    result = 0
    current = 0
        
    for c in s:
        if c == '1':
            current += 1
        else:
            result += (current + 1) * current // 2
            current = 0
                
    result += (current + 1) * current // 2
        
    return result

print(numSub("0110111"))
print(numSub("111111"))