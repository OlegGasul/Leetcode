def isSubstring(s1, s2):
    def build_pattern(string):
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

    def does_match(string, substring, pattern):
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

    return does_match(s2, s1, build_pattern(s1))

# print(isSubstring("aaab", "aaanaaamaaab"))
print(isSubstring("10", "0110"))