def queryString(s: str, n: int) -> bool:
    def isSubstring(s1):
        def buildPattern(string):
            pattern = [0 for s in string] 
            j = 0
            i = 1
        
            while i < len(string):
                if string[i] == string[j]:
                    pattern[i] = j + 1
                    i += 1
                    j += 1
                elif j > 0:
                    j = pattern[j-1]
                else:
                    i += 1
            return [-1] + pattern

        def doesMatch(string, substring, pattern):
            i = 0
            j = 0
        
            while i < len(string):
                if string[i] == substring[j]:
                    if j == len(substring) - 1:
                        return True
                    i += 1
                    j += 1
                elif j > 0:
                    j = pattern[j]
                else: 
                    i += 1
            return False

        return doesMatch(s, s1, buildPattern(s1))

    while n:
        value = bin(n)[2:]
        
        if not isSubstring(value):
            return False
            
        n -= 1
            
    return True

print(queryString("0110", 3))
            