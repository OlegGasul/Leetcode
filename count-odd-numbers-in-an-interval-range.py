class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return low % 2

        result = 0
        
        if low % 2 != 0:
            low += 1
            result += 1
        
        if high % 2 != 0:
            high -= 1
            result += 1

        return result + (high - low) // 2

solution = Solution()
assert solution.countOdds(3, 7) == 3
assert solution.countOdds(8, 10) == 1