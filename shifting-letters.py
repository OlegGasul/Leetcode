def shiftingLetters(s: str, shifts):
    first = ord('a')
    last = ord('z')

    i = len(shifts) - 1
    while i >= 0 and len(shifts) > 0:
        if i < len(shifts) - 1:
            shifts[i] += shifts[i + 1]
        shifts[i] %= 26
        
        i -= 1

    arr = list(s)
    for i in range(len(arr)):
        if shifts[i] == 0:
            continue
        
        value = ord(arr[i]) + shifts[i]
        if value > last:
            value = first + (value - last - 1)
        arr[i] = chr(value)

    return ''.join(arr)
        

print(shiftingLetters("abc", [3, 5, 9]))
print(shiftingLetters("aaa", [1, 2, 3]))
print(shiftingLetters("abc", [33, 35, 39]))
print(shiftingLetters("ruu", [26, 9, 17]))
