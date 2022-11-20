class Solution:
    def minTaps(self, n: int, ranges) -> int:
        max_range = [0] * (n + 1)
        
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)

        # it's a jump game now
        start = end = step = 0
        
        while end < n:
            step += 1
            start, end = end, max(i + max_range[i] for i in range(start, end + 1))
            if start == end:
                return -1
            
        return step

solution = Solution()
print(solution.minTaps(9, [0, 5, 0, 3, 3, 3, 1, 4, 0, 4]))
print(solution.minTaps(7, [1, 2, 1, 0, 2, 1, 0, 1]))
print(solution.minTaps(5, [3, 4, 1, 1, 0, 0]))
print(solution.minTaps(3, [0, 0, 0, 0]))