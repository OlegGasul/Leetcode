class Solution:
    def minNumberOperations(self, target) -> int:
        result = 0
        free = 0

        for i in range(len(target)):
            if target[i] > free:
                result += target[i] - free
                free = target[i]
            elif target[i] < free:
                free = target[i]

        return result

solution = Solution()
print(solution.minNumberOperations([3, 1, 5, 4, 2]))
print(solution.minNumberOperations([3, 1, 1, 2]))