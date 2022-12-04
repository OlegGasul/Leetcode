class Solution:
    def minimumHealth(self, damage, armor: int) -> int:
        if armor == 0:
            return sum(damage) + 1
        
        total = sum(damage)
        maximum = max(damage)
        
        total -= maximum
        maximum -= min(armor, maximum)

        return total + maximum + 1

solution = Solution()
assert solution.minimumHealth([2, 7, 4, 3], 4) == 13
assert solution.minimumHealth([2, 5, 3, 4], 7) == 10