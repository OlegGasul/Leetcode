class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        positiveDiag = set()
        negativeDiag = set()

        result = 0

        def backtrack(row):
            nonlocal result

            if row == n:
                result += 1
                return

            for col in range(n):
                if col in cols or row + col in positiveDiag or row - col in negativeDiag:
                    continue
                
                cols.add(col)
                positiveDiag.add(row + col)
                negativeDiag.add(row - col)
                
                backtrack(row + 1)

                cols.remove(col)
                positiveDiag.remove(row + col)
                negativeDiag.remove(row - col)

        backtrack(0)

        return result

solution = Solution()
print(solution.totalNQueens(6))