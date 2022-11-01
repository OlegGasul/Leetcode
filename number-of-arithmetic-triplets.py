class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        visited = set()
        result = 0
        
        for num in nums:
            if num - diff in visited and num - 2 * diff in visited:
                result += 1
            visited.add(num)
                
        return result

solution = Solution()
print(solution.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
print(solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
print(solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 3))