import functools

def getKth(lo: int, hi: int, k: int) -> int:
    def getPowerValue(num):
        result = 0
            
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = num * 3 + 1
            result += 1
            
        return result
        
    result = []
        
    for num in range(lo, hi + 1):
        result.append([getPowerValue(num), num])
            
    def compare(a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]
        
    result = sorted(result, key = functools.cmp_to_key(compare))
        
    return result[k - 1][1]

print(getKth(12, 15, 2))
print(getKth(7, 11, 4))