class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        left = 1
        right = n

        while left < right:
            pivot = left + (right - left) // 2
            
            a = pivot * (pivot + 1) / 2
            b = (pivot + n) / 2 * (n - pivot + 1)

            if a == b:
                return pivot
            
            if a < b:
                left = pivot + 1
            else:
                right = pivot - 1

        return -1

solution = Solution()
assert solution.pivotInteger(8) == 6
assert solution.pivotInteger(1) == 1
assert solution.pivotInteger(4) == -1