class Solution:
    def countTime(self, time: str) -> int:
        h1 = time[0]
        h2 = time[1]
        result1 = 1

        if h1 == "?" and h2 == "?":
            result1 = 24
        else:
            if h1 == "?":
                result1 = 3 if int(h2) < 4 else 2
            elif h2 == "?":
                result1 = 10 if int(h1) < 2 else 4

        m1 = time[3]
        m2 = time[4]
        result2 = 1

        if m1 == "?":
            result2 = 6
        if m2 == "?":
            result2 *= 10
        
        return result1 * result2

solution = Solution()
assert solution.countTime("?5:00") == 2
assert solution.countTime("0?:0?") == 100
assert solution.countTime("??:??") == 1440