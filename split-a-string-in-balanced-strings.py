def balancedStringSplit(s: str) -> int:
    balance = 0
    result = 0
        
    for i in range(len(s)):
        balance += 1 if s[i] == "L" else -1
        if balance == 0:
            result += 1
                
    return result

print(balancedStringSplit("RLRRLLRLRL"))
print(balancedStringSplit("RLRRRLLRLL"))