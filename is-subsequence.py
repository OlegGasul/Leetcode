def isSubsequence(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
        
    if len(s) == 0:
        return True

    dp = [1]
    s = list(s)
    
    i = 1
    while i < len(s):
        if s[i] == s[i - 1]:
            dp[-1] += 1
            s.pop(i)
        else:
            dp.append(1)
            i += 1

    current = 0
    for i in range(len(t)):
        if t[i] == s[current]:
            dp[current] -= 1
            if dp[current] == 0:
                current += 1
                if current > len(s) - 1:
                    return True

    return False


print(isSubsequence("aabc", "ahabgdc"))
print(isSubsequence("axc", "ahbgdc"))