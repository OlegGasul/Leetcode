def reverseString(s):
    length = len(s)
    middle = length // 2
    
    for i in range(0, middle):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]

s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)
