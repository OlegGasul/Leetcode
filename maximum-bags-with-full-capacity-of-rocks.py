class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks: int) -> int:
        deficit = []
        result = 0

        for i in range(len(capacity)):
            val = capacity[i] - rocks[i]
            if val == 0:
                result += 1
                continue
            deficit.append(val)

        deficit.sort()

        while deficit and additionalRocks:
            val = deficit.pop(0)
            
            if additionalRocks < val:
                break

            additionalRocks -= val
            result += 1

        return result

solution = Solution()
print(solution.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))
print(solution.maximumBags([10, 2, 2], [2, 2, 0], 100))