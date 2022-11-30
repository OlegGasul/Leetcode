class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        n = len(calories)
        prefixSum = [0] * (n + 1)

        points = 0

        for i in range(n):
            prefixSum[i] = prefixSum[i - 1] + calories[i]
        
        for i in range(k - 1, n):
            current = prefixSum[i] - prefixSum[i - k]
            
            if current < lower:
                points -= 1
            elif current > upper:
                points += 1
        
        return points

solution = Solution()
assert solution.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3) == 0