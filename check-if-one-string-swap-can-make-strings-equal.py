class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        
        indecies = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indecies.append(i)
                if len(indecies) > 2:
                    return False
        
        if len(indecies) < 2:
            return False
        
        return s2[indecies[0]] == s1[indecies[1]] and s2[indecies[1]] == s1[indecies[0]]

solution = Solution()
assert solution.areAlmostEqual("bank", "kanb") == True
assert solution.areAlmostEqual("attack", "defend") == False
assert solution.areAlmostEqual("kelb", "kelb") == True