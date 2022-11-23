class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in squares[i // 3][j // 3]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                squares[i // 3][j // 3].add(num)

        return True

solution = Solution()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))