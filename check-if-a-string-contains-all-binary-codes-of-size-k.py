def hasAllCodes(s: str, k: int) -> bool:
    unique = set()
    total = 2 ** k

    for i in range(len(s) - k + 1):
        unique.add(s[i : i + k])
        if len(unique) == total:
            return True
            
    return False

print(hasAllCodes("00110110", 2))
print(hasAllCodes("0110", 1))
print(hasAllCodes("0110", 2))