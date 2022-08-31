def findTheLongestSubstring(s: str) -> int:
    vowels = { "a": 1, "e": 2, "i": 4, "o": 8, "u": 16 }
    dict1, cur, max_len = {0: -1}, 0, 0
    
    for i, c in enumerate(s):
        if c in vowels:
            cur = cur^vowels[c]
        if cur not in dict1:
            dict1[cur] = i
            print(dict1)
        else:
            max_len = max(max_len, i - dict1[cur])
            
    return max_len


print(findTheLongestSubstring("eleetminicoworoep"))