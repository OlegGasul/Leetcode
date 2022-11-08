class Solution:
    def findMinDifference(self, timePoints) -> int:
        def timeToMin(time):
            return int(time[:2]) * 60 + int(time[3:])

        dp = [False] * (24 * 60)

        minTime = 24 * 60
        maxTime = -1

        for time in timePoints:
            mins = timeToMin(time)
            if dp[mins]:
                return 0
            
            dp[mins] = True

            minTime = min(minTime, mins)
            maxTime = max(maxTime, mins)

        result = ((24 * 60) - maxTime) + minTime
        if result == 1:
            return 1

        prev = minTime
        for time in range(minTime + 1, maxTime + 1):
            if not dp[time]:
                continue
            
            result = min(result, time - prev)
            prev = time

        return result

solution = Solution()
print(solution.findMinDifference(["23:59", "00:00"]))