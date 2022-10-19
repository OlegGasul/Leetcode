def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ""
        
    if len(strs) == 1:
        return strs[0]
        
    result = ""
        
    i = 0
    while i < len(strs[0]):
        for j in range(1, len(strs)):
            if i >= len(strs[j]):
                return result
                
            if strs[j][i] != strs[0][i]:
                return result
                
        result += strs[0][i]
        
        i += 1
            
    return result

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))