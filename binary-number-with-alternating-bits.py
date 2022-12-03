class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        
        while n:
            if prev != None:
                if n & 1 == prev:
                    return False
            
            prev = n & 1
            n >>= 1
        
        return True

solution = Solution()
assert solution.hasAlternatingBits(5) == True
assert solution.hasAlternatingBits(7) == False
assert solution.hasAlternatingBits(11) == False