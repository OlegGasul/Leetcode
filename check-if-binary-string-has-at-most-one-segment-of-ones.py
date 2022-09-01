def checkOnesSegment(s: str) -> bool:
    n = int(s, 2)
        
    one = False
    while n:
        if n & 1 == 1:
            one = True
        elif n & 1 == 0 and one:
            return False
            
        n >>= 1
            
    return one

print(checkOnesSegment("1001"))
print(checkOnesSegment("110"))
print(checkOnesSegment("000"))
print(checkOnesSegment("001"))