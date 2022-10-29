def checkDistances(s: str, distance) -> bool:
    a = ord('a')
    indecies = [-1] * 26
        
    for i in range(len(s)):
        index = ord(s[i]) - a
            
        if indecies[index] == -1:
            indecies[index] = i
            continue
            
        if i - indecies[index] - 1 != distance[index]:
            return False
            
    return True

print(checkDistances("abaccb", [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(checkDistances("aa", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))