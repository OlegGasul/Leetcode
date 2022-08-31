def getLucky(s: str, k: int) -> int:
    a = ord('a')
        
    letters = list(s)
    for i in range(len(letters)):
        letters[i] = str(ord(letters[i]) - a + 1)
            
    def transform(value):
        return sum([int(x) for x in list(str(value))])

    value = int(''.join(letters))

    while k:
        value = transform(value)
        k -= 1

    return value

print(getLucky("iiii", 1))