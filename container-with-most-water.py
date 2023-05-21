class Solution:
    def maxArea(self, height) -> int:
        size = len(height)
        if size < 2:
            return -1
        
        left = 0
        right = size - 1

        result = 0
        
        while left < right:
            leftValue = height[left]
            rightValue = height[right]
            
            volume = (right - left) * min(leftValue, rightValue)
            result = max(volume, result)

            if leftValue < rightValue:
                left += 1
            else:
                right -= 1
        
        return result

solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([1, 1]) == 1