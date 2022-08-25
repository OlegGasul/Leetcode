def checkIfCanBreak(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    a = sorted(s1)
    b = sorted(s2)
    
    result = True

    for i in range(len(a)):
        if a[i] < b[i]:
            result = False
            break

    if result:
        return True

    result = True

    for i in range(len(a)):
        if b[i] < a[i]:
            return False

    return True

print(checkIfCanBreak("leetcodee", "interview"))
print(checkIfCanBreak("abc", "xya"))