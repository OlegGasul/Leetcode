def digitSum(s: str, k: int) -> str:
    if len(s) < k:
        return s

    while k < len(s):
        i = 0
        arr = []
        
        while i < len(s):
            amount = sum(map(int, list(s[i : min(i + k, len(s))])))
            arr.append(str(amount))

            i += k
        
        s = ''.join(arr)

    return s

print(digitSum("11111222223", 3))
print(digitSum("00000000", 3))