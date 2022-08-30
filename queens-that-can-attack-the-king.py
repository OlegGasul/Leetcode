def queensAttacktheKing(queens, king):
    length = 8
    
    board = [[0 for x in range(length)] for y in range(length)] 
    board[king[0]][king[1]] = 1

    board[queens[0][0]][queens[0][1]] = 2

    for queen in queens:
        board[queen[0]][queen[1]] = 2

    result = []

    def checkDirection(iIncr, jIncr):
        i = king[0]
        j = king[1]

        while i >= 0 and i < length and j >= 0 and j < length:
            if board[i][j] == 2:
                result.append([i, j])
                break

            i += iIncr
            j += jIncr

    i = king[0]
    j = king[1]
    checkDirection(0, 1)
    checkDirection(1, 1)
    checkDirection(1, 0)
    checkDirection(1, -1)
    checkDirection(0, -1)
    checkDirection(-1, -1)
    checkDirection(-1, 0)
    checkDirection(-1, 1)

    return result


print(queensAttacktheKing([[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0]))

# [2, 0, 0, 0, 0, 0, 0, 0]
# [0, 2, 0, 0, 0, 0, 0, 0]
# [0, 0, 2, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 2, 2, 0, 0]
# [0, 0, 0, 0, 2, 2, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
print(queensAttacktheKing([[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], [3, 3]))

print(queensAttacktheKing([[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], [3, 4]))

