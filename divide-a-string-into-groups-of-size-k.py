def divideString(s: str, k: int, fill: str):
    length = len(s)
    result = []
        
    i = 0
    while i < length:
        result.append(s[i : i + k])
        i += k
    
    if len(result[-1]) < k:
        result[-1] = result[-1].ljust(k, fill)
        
    return result

print(divideString("ctoyjrwtngqwt", 8, "n"))