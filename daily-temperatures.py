class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                t, index = stack.pop()
                result[index] = i - index
            
            stack.append([temperatures[i], i])

        return result

solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(solution.dailyTemperatures([30, 40, 50, 60]))
print(solution.dailyTemperatures([30, 60, 90]))
