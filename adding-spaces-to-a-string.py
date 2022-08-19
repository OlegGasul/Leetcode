def addSpaces(s: str, spaces) -> str:
    if s == None or s == "":
        return ""

    if spaces == None or len(spaces) == 0:
        return s
    
    spaces = sorted(spaces)
        
    length = len(s)
    prev = 0
    arr = []
    
    for x in spaces:
        if x > length:
            break
            
        arr.append(s[prev : x])
        prev = x

    arr.append(s[prev : length])

    return ' '.join(arr)


print(addSpaces("LeetcodeHelpsMeLearn", [7, 8, 13, 15, 100]))
print(addSpaces("LeetcodeHelpsMeLearn", [100]))
print(addSpaces("LeetcodeHelpsMeLearn", []))
print(addSpaces(None, [7, 8, 13, 15, 100]))
print(addSpaces(None, [7, 8, 13, 15, 100]))