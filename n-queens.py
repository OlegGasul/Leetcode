class Solution:
    def solveNQueens(self, n: int):
        cols = set()
        positiveDiag = set()
        negativeDiag = set()

        result = []

        board = [['.'] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                copy = [''.join(r) for r in board]
                result.append(copy)
                return

            for col in range(n):
                if col in cols or row + col in positiveDiag or row - col in negativeDiag:
                    continue
                
                cols.add(col)
                positiveDiag.add(row + col)
                negativeDiag.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                positiveDiag.remove(row + col)
                negativeDiag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)

        return result

solution = Solution()
print(solution.solveNQueens(6))