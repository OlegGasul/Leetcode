def hasAllCodes(s: str, k: int) -> bool:
    unique = set()
        
    for i in range(len(s) - k + 1):
        unique.add(s[i : i + k])
            
    return len(unique) == 2 ** k

print(hasAllCodes("00110110", 2))
print(hasAllCodes("0110", 1))
print(hasAllCodes("0110", 2))