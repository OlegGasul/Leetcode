def diagonalSum(mat) -> int:
    length = len(mat)

    if length == 1:
        return mat[0][0]
        
    result = 0
        
    for i in range(length):
        result += mat[i][i] + mat[i][length - i - 1]
            
    if length % 2 == 1:
        middle = length // 2
        result -= mat[middle][middle]
            
    return result

print(diagonalSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]))

print(diagonalSum([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]]))

print(diagonalSum([[5]]))