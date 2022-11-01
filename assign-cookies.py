class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        result = 0
        
        while g and s:
            while s and g[-1] > s[-1]:
                s.pop()
                
            if not s or not g:
                break
            
            g.pop()
            s.pop()
            result += 1
            
        return result

solution = Solution()
print(solution.findContentChildren([1, 2, 3], [1, 1]))
print(solution.findContentChildren([1, 2], [1, 2, 3]))