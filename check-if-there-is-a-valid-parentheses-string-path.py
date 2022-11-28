from collections import defaultdict

class Solution:
    def hasValidPath(self, grid) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        if (rows + cols) % 2 == 0:
            return False
        
        if grid[-1][-1] == "(":
            return False
        
        if grid[0][0] == ")":
            return False

        dp = defaultdict(set)
        dp[0, -1] = dp[-1, 0] = {0}

        for i in range(rows):
            for j in range(cols):
                d = 1 if grid[i][j] == '(' else -1
                dp[i, j] |= { a + d for a in dp[i - 1, j] | dp[i, j - 1] if a + d >= 0 }
        
        return 0 in dp[rows - 1, cols - 1]

solution = Solution()
assert solution.hasValidPath([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]) == True
assert solution.hasValidPath([[")", ")"], ["(", "("]]) == False