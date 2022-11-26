class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left = 2
        right = num // 2

        while left <= right:
            middle = left + (right - left) // 2
            value = middle ** 2
            
            if num == value:
                return True

            if value > num:
                right = middle - 1
            else:
                left = middle + 1

        return False

solution = Solution()
assert solution.isPerfectSquare(16) == True
assert solution.isPerfectSquare(100) == True
assert solution.isPerfectSquare(7) == False