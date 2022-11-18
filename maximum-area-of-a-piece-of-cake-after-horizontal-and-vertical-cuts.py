class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        hh = []
        prev = 0
        maxH = float('-inf')
        for n in horizontalCuts + [h]:
            maxH = max(maxH, n - prev)
            prev = n

        vh = []
        prev = 0
        maxW = float('-inf')
        for n in verticalCuts + [w]:
            maxW = max(maxW, n - prev)
            prev = n

        return maxH * maxW % (10 ** 9 + 7)

solution = Solution()
print(solution.maxArea(5, 4, [1, 2, 4], [1, 3]))
print(solution.maxArea(5, 4, [3, 1], [1]))