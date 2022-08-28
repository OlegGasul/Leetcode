from time import sleep
import copy

def solveSudoku(board):
    numbers = set(range(1, 10))
    
    length = 9
    squareLength = 3

    for i in range(length):
        for j in range(length):
            board[i][j] = int(board[i][j]) if board[i][j].isdigit() else 0

    print()
    print(board)

    squares = [[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]
    rows = [set(numbers)] * length
    cols = [set(numbers)] * length

    def fillSquares():
        nonlocal board

        for i in range(squareLength):
            for j in range(squareLength):
                nums = set()
                for k in range(i * squareLength, i * squareLength + squareLength):
                    for l in range(j * squareLength, j * squareLength + squareLength):
                        if board[k][l] != 0:
                            nums.add(board[k][l])
                squares[i][j] = numbers - nums
    fillSquares()

    def recalculateSquare(i, j):
        squares[i // squareLength][j // squareLength] -= set([board[i][j]])                

    def recalculateRow(i):
        nums = set()
        for j in range(length):
            if type(board[i][j]) is set:
                continue
            nums.add(board[i][j])
        rows[i] -= nums

    def recalculateCol(j):
        nums = set()
        for i in range(length):
            if type(board[i][j]) is set:
                continue
            nums.add(board[i][j])
        cols[j] -= nums

    def recalculateBoard():
        indexes = set()

        for i in range(length):
            for j in range(length):
                if not type(board[i][j]) is set:
                    continue
            
                value = rows[i].intersection(cols[j]).intersection(squares[i // squareLength][j // squareLength])
                if len(value) == 1:
                    indexes.add(tuple((i, j)))
                    board[i][j] = list(value)[0]
                else:
                    board[i][j] = value

        return indexes

    for i in range(length):
        nums = set()
        for j in range(length):
            if board[i][j] != 0:
                nums.add(board[i][j])
        rows[i] = numbers - nums

    for j in range(length):
        nums = set()
        for i in range(length):
            if board[i][j] != 0:
                nums.add(board[i][j])

        cols[j] = numbers - nums

    indexes = set()

    for i in range(length):
        for j in range(length):
            if board[i][j] != 0:
                indexes.add(tuple((i, j)))
                continue
            
            value = rows[i].intersection(cols[j]).intersection(squares[i // squareLength][j // squareLength])
            if len(value) == 1:
                indexes.add(tuple((i, j)))
                board[i][j] = list(value)[0]
            else:
                board[i][j] = rows[i].intersection(cols[j]).intersection(squares[i // squareLength][j // squareLength])

    
    while indexes:
        for pair in indexes:
            recalculateSquare(pair[0], pair[1])
            recalculateRow(pair[0])
            recalculateCol(pair[1])

        indexes = recalculateBoard()

    print()
    print('rows')
    print(rows)
    print()
    print('cols')
    print(cols)
    print()
    print('squares')
    print(squares)
    print()

    # for i in range(length):
    #     for j in range(length):
    #         if type(board[i][j]) is set:

    


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
# solveSudoku(board)

board = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]]
print(board)
solveSudoku(board)
print(board)