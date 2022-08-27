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

assert divideString("ctoyjrwtngqwt", 8, "n") == ['ctoyjrwt', 'ngqwtnnn']
assert divideString("abcdefghij", 3, "x") == ['abc', 'def', 'ghi', 'jxx']
assert divideString("abcdefghij", 1, "x") == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']