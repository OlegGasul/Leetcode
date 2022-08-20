def thousandSeparator(n: int) -> str:
    s = str(n)
    if n < 1000:
        return s

    result = ''
    pointer = len(s)
    
    while pointer > 3:
        result = '.' + s[pointer - 3 : pointer] + result
        pointer -= 3

    result = s[0 : pointer] + result

    return result


print(thousandSeparator(987))
print(thousandSeparator(1234))
print(thousandSeparator(12345678910))