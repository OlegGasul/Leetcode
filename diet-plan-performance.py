class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        current = 0

        for i in range(k):
            current += calories[i]
        
        points = 0
        if current < lower:
            points -= 1
        elif current > upper:
            points += 1
        
        for i in range(k, len(calories)):
            current += calories[i]
            current -= calories[i - k]
            if current < lower:
                points -= 1
            elif current > upper:
                points += 1
        
        return points

solution = Solution()
assert solution.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3) == 0