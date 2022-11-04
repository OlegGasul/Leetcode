class Solution:
    def minPartitions(self, n: str) -> int:
        nums = [int(x) for x in list(n)]
        
        result = 0
        current = 0
        
        for i in reversed(range(len(nums))):
            if nums[i] > current:
                result += nums[i] - current
                current = nums[i]
                
        return result

solution = Solution()
assert solution.minPartitions("32") == 3
assert solution.minPartitions("27346209830709182346") == 9