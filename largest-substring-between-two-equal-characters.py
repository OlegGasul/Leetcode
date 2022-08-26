def maxLengthBetweenEqualCharacters(s: str) -> int:
    indexes = {}
    result = -1
        
    for i in range(len(s)):
        if not s[i] in indexes:
            indexes[s[i]] = [i, i]

        values = indexes[s[i]]
        indexes[s[i]] = [min(i, values[0]), max(i, values[1])]
            
        values = indexes[s[i]]
        if values[0] != values[1]:
            result = max(result, values[1] - values[0] - 1)
            

    return result
        

print(maxLengthBetweenEqualCharacters("abcavvvb"))
print(maxLengthBetweenEqualCharacters("cbzxy"))
print(maxLengthBetweenEqualCharacters("abca"))