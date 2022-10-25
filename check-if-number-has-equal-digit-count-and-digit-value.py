from collections import Counter

def digitCount(num: str) -> bool:
    counter = Counter(num)
        
    for i in range(len(num)):
        if counter[str(i)] != int(num[i]):
            return False
            
    return True

print(digitCount("1210"))
print(digitCount("030"))