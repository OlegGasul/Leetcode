class Solution:
    def countElements(self, arr) -> int:
        nums = set(arr)

        result = 0
        
        for num in arr:
            if num + 1 in nums:
                result += 1

        return result

solution = Solution()
print(solution.countElements([1, 2, 3]))
print(solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]))