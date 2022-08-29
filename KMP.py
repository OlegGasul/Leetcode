def isSubstring(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    dp = [0] * len1
    i = 0
    j = 1
    while j < len1:
        if s1[i] == s1[j]:
            i += 1
            dp[j] = i
            j += 1
        elif i == 0:
            dp[j] = 0
            j += 1
        else:
            i = dp[i - 1]
    
    print(dp)

    i = 0
    j = 1

    while i < len1 and j < len2:
        if s1[i] == s2[j] and i == len1 - 1:
            return True
        elif s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i = dp[i - 1]
            if i == 0:
                j += 1

    return False

print(isSubstring("aaab", "aaanaaamaaab"))