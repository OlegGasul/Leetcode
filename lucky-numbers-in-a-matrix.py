def luckyNumbers(matrix):
    minRows = [min(x) for x in matrix]
    
    maxColumns = []
    
    for i in range(len(matrix[0])):
        tmp = []
        for j in range(len(matrix)):
            tmp.append(matrix[j][i])
        maxColumns.append(max(tmp))


    return set(minRows) & set(maxColumns)


print(luckyNumbers([
    [1, 10, 4, 2],
    [9, 3, 8, 7],
    [15, 16, 17, 12]]))

print(luckyNumbers([
    [9, 3, 8, 7],
    [1, 10, 4, 2],
    [15, 16, 17, 12]]))

print(luckyNumbers([
    [3, 7, 8],
    [9, 11, 13],
    [15, 16, 17]]))

print(luckyNumbers([
    [7, 8],
    [1, 2]]))

print(luckyNumbers([
    [3, 6],
    [7, 1],
    [5, 2],
    [4, 8]]))