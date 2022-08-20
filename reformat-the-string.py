def reformat(s: str) -> str:
    digits = []
    letters = []

    for x in s:
        if x.isdigit():
            digits.append(x)
        else:
            letters.append(x)

    letersLen = len(letters)
    digitsLen = len(digits)

    if abs(letersLen - digitsLen) > 1:
        return ""

    (largest, smallest) = (letters, digits) if letersLen > digitsLen else (digits, letters)

    result = []

    while largest and smallest:
        result.append(largest.pop())
        result.append(smallest.pop())
    
    while largest:
        result.append(largest.pop())


    return ''.join(result)

print(reformat("a0b1c2"))
print(reformat("abc01234"))
print(reformat("abcd01234"))
print(reformat("abcdef01234"))
print(reformat("covid2019"))