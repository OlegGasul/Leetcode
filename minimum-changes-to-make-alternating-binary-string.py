def minOperations(s: str) -> int:
    fromZero = 0
    fromOne = 0
        
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "0":
                fromOne += 1
            else:
                fromZero += 1
        else:
            if s[i] == "0":
                fromZero += 1
            else:
                fromOne += 1
                    
    return min(fromZero, fromOne)

print(minOperations("0100"))
print(minOperations("10"))
print(minOperations("1111"))