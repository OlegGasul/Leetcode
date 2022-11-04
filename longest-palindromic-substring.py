# TODO learn Manacher's Algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        if len(s) == 1:
            return s[0]
        
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
            
        
        result = ""
        longest = float('-inf')
        
        def extend(index1, index2):
            while index1 > 0 and index2 < len(s) - 1:
                if s[index1 - 1] != s[index2 + 1]:
                    return s[index1 : index2 + 1]
                
                index1 -= 1
                index2 += 1
                
            return s[index1 : index2 + 1]
        
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            pal = extend(i, j)
            
            if len(pal) > longest:
                result = pal
                longest = len(pal)
                
            j += 1
            if j >= len(s):
                break
            
            if s[i] != s[j]:
                i = j
                
        return result

solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))