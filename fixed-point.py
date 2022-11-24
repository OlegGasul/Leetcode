class Solution:
    def fixedPoint(self, arr) -> int:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            middle = left + (right - left) // 2
            if arr[middle] == middle:
                right = middle
            elif arr[middle] < middle:
                left = middle + 1
            else:
                right = middle - 1
        
        if arr[left] == left:
            return left
        elif arr[right] == right:
            return right
        else:
            return -1

solution = Solution()
print(solution.fixedPoint([-10, -5, -2, 0, 4, 5, 6, 7, 8, 9, 10]))
print(solution.fixedPoint([-10, -5, 2, 3, 7]))
