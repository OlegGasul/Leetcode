class Solution:
    def trap(self, height) -> int:
        length = len(height)
        if length < 3:
            return 0

        left = 0
        right = length - 1

        leftMax = height[left]
        rightMax = height[right]

        result = 0

        while left < right:
            if leftMax < rightMax:
                current = height[left + 1]

                result += max(0, leftMax - current)
                
                leftMax = max(leftMax, current)
                left += 1
            else:
                current = height[right - 1]
                
                result += max(0, rightMax - current)
                
                rightMax = max(rightMax, current)
                right -= 1

        return result

solution = Solution()
assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution.trap([4, 2, 0, 3, 2, 5]) == 9