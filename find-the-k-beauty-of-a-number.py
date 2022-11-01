class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        
        s = str(num)
        
        i = 0
        while i <= len(s) - k:
            n = int(s[i : i + k])
            if n == 0:
                i += 1
                continue
            
            if num % n == 0:
                result += 1
                
            i += 1
                
        return result

solution = Solution()
print(solution.divisorSubstrings(430043, 2))
print(solution.divisorSubstrings(30003, 3))