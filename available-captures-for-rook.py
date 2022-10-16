# On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.
# 
# When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.
# 
# Return the number of available captures for the white rook.

def numRookCaptures(board) -> int:
    length = 8
        
    rookI = -1
    rookJ = -1
        
    for i in range(length):
        for j in range(length):
            if board[i][j] == "R":
                rookI = i
                rookJ = j
                break

    if rookI < 0 or rookJ < 0:
        return 0
    
    empty = "."
    pawn = "p"

    result = 0

    # Right
    j = rookJ + 1
    while j < length:
        if board[rookI][j] == empty:
            j += 1
            continue
            
        if board[rookI][j] == pawn:
            result += 1
            break
            
        break
        
    # Left
    j = rookJ - 1
    while j >= 0:
        if board[rookI][j] == empty:
            j -= 1
            continue
            
        if board[rookI][j] == pawn:
            result += 1
            break
                
        break
            
    # Down
    i = rookI + 1
    while i < length:
        if board[i][rookJ] == empty:
            i += 1
            continue
            
        if board[i][rookJ] == pawn:
            result += 1
            break
                
        break
            
    # Top
    i = rookI - 1
    while i >= 0:
        if board[i][rookJ] == empty:
            i -= 1
            continue
            
        if board[i][rookJ] == pawn:
            result += 1
            break
                
        break
            
    return result

print(numRookCaptures([
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]]
))
