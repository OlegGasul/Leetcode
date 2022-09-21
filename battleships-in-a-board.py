def countBattleships(board) -> int:
    rows = len(board)
    cols = len(board[0])
        
    result = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "X":
                if i == 0 and j == 0:
                    result += 1
                    continue

                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue

                result += 1
                    
    return result

print(countBattleships([
    [".","X",".",".","X"],
    [".","X",".",".","X"],
    [".",".",".",".","X"],
    ["X",".","X","X","."],
    ["X",".",".",".","X"]]))