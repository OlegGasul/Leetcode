from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a = []
        indecies = defaultdict(int)

        for i in range(len(s)):
            if s[i] in indecies:
                a.append(indecies[s[i]])
            else:
                indecies[s[i]] = i
                a.append(i)
        
        b = []
        indecies = defaultdict(int)

        for i in range(len(t)):
            if t[i] in indecies:
                b.append(indecies[t[i]])
            else:
                indecies[t[i]] = i
                b.append(i)

        return a == b

solution = Solution()
assert solution.isIsomorphic("egg", "add") == True
assert solution.isIsomorphic("foo", "bar") == False
assert solution.isIsomorphic("paper", "title") == True