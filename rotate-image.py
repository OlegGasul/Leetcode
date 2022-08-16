# https://leetcode.com/problems/rotate-image/

def exchange(startI, startJ, matrix):
    length = len(matrix)

    prevI = startI
    prevJ = startJ
    prev = matrix[prevI][prevJ]

    for n in range(4):
        i = prevJ
        j = length - prevI - 1

        temp = matrix[i][j]
        
        matrix[i][j] = prev
        
        prevI = i
        prevJ = j
        prev = temp


def rotate(matrix):
    length = len(matrix[0])

    i = 0
    while i < length - i - 1:
        j = i

        while j < length - i - 1:
            exchange(i, j, matrix)
            j += 1

        i += 1
        
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

rotate(matrix)

print(matrix)
