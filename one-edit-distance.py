class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
        
        ns = len(s)
        nt = len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if abs(nt - ns) > 1:
            return False
        
        for i in range(ns):
            if s[i] == t[i]:
                continue
            
            if ns == nt:
                return s[i + 1 : ] == t[i + 1 : ]
            else:
                return s[i :] == t[i + 1 : ]

        return ns + 1 == nt

solution = Solution()
assert solution.isOneEditDistance("ab", "acb") == True
assert solution.isOneEditDistance("", "") == False