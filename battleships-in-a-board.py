def countBattleships(board) -> int:
    rows = len(board)
    cols = len(board[0])
        
    def mark(i, j, incrI, incrJ):
        if incrI == 0 and incrJ == 0:
            board[i][j] = "."
            return
            
        while i < rows and i >= 0 and j < cols and j >= 0:
            if board[i][j] == ".":
                return
            
            board[i][j] = "."
            
            i += incrI
            j += incrJ
                
    result = 0        
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "X":
                result += 1
                    
                incrI = 0
                incrJ = 0
                    
                if j + 1 < cols and board[i][j + 1] == "X":
                    incrJ = 1
                elif i + 1 < rows and board[i + 1][j] == "X":
                    incrI = 1
                        
                mark(i, j, incrI, incrJ)
                    
    return result

print(countBattleships([
    [".","X",".",".","X"],
    [".","X",".",".","X"],
    [".",".",".",".","X"],
    ["X",".","X","X","."],
    ["X",".",".",".","X"]]))